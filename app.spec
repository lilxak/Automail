# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Users\\yasser\\Desktop\\aiesec\\Aiesec Babez Mailer'],
             binaries=[],
             datas=[('C:\\Users\\yasser\\AppData\\Local\\Python-Eggs\\Python-Eggs\\Cache\\eel-0.12.2-py3.8.egg-tmp\\eel\\eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
