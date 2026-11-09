# -*- coding: utf-8 -*-
"""Lint Provimento 205 (motor da Serya) sobre os textos do gen.py, nos 3 idiomas.
Uso: python3 lint.py   (sai com código 1 se houver erro não liberado)"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '10-motor'))
from gen_cliente import lint_provimento  # noqa: E402

# Menções a plantão 24h / 24/7 aprovadas pelo cliente (commit aa96a59). Só esta regra é liberada, e só nestas chaves.
LINT_ALLOW = {'wa_btn', 'ix_title', 'ix_desc', 'hero_badge', 'urg_cta', 'in_en', 'ct_f_micro',
              'cr_title', 'cr_desc', 'cr_cta', 'cr_band_p', 'il_desc', 'il_how_box', 'il_band_p'}
REGRA_24H = "'plantão/atendimento 24h'"

src = open(os.path.join(HERE, 'gen.py'), encoding='utf-8').read().split("if __name__ == '__main__':")[0]
ns = {'__file__': os.path.join(HERE, 'gen.py')}
exec(src, ns)
falhas = 0
for lg, t in ns['LANGS'].items():
    news = [{'veiculo': n['veiculo'], 'texto': n[lg]} for n in ns['NEWS']]
    erros, avisos = lint_provimento({'conteudo': {k: v for k, v in t.items() if not k.startswith('_')}, 'news': news})
    liberados = [e for e in erros if REGRA_24H in e and e.split(':')[0].split('.')[-1] in LINT_ALLOW]
    erros = [e for e in erros if e not in liberados]
    print('== %s: %d erro(s), %d aviso(s), %d liberado(s) (plantão aprovado)' % (lg, len(erros), len(avisos), len(liberados)))
    for e in erros: print('  ERRO ', e)
    for w in avisos: print('  aviso', w)
    falhas += len(erros)
sys.exit(1 if falhas else 0)
