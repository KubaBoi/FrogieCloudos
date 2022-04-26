# File Browser Server

## Instalation

- pip install PyAutoGUI
- pip install Send2Trash
- pip install Pillow
- pip install pywin32

## TODO

- [x] float menu muze vylezt mimo obrazovku
- [ ] pripojeni na FrogieCloudos
    - [x] pripravit pro autorizaci z jinych zdroju
    - [ ] predelat Frogie Cloudos aby odpovidal API FileBrowserServeru
- [ ] dragAndDrop pro okna
    - [ ] mozna udelat dalsi moznost gridStyle pro free movement
        - po rozdeleni do gridu ulozit pozice oken, zrusit grid a nastavit pozice oken z ulozenych hodnot?
- [x] oznacit not found okna

## kill process

- netstat -ano | findstr :7999
- taskkill /PID <PID> /F