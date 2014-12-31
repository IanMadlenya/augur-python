# -*- mode: python -*-

a = Analysis(['threads.py'],
             pathex=[os.path.join(os.environ.get('AUGURROOT', None), 'augur', 'core')],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

a.datas += [('demo', 'demo', 'DATA')]
a.datas += [('errors', 'errors', 'DATA')]
a.datas += [('log', 'log', 'DATA')]
a.datas += [('README.md', 'README.md', 'DATA')]

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='core.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='core')
