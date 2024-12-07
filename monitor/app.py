import os
import pathlib

def main():
    # if os.path.exists('file'):
    #     print( 'The file exists' )
    # else:
    #     print( 'The file does not exist' )
    # Можна безпосередньо перевірити, чи існує шлях до файлу:
    # exists = os.path.isfile('files' )
    # if exists:
    #     # Store configuration file valuesfile
    #     print( 'The file exists' )
        
    #     pass
    # else:
    #     # Keep presets
    #     print( 'Keep presets' )
    #     pass

    # with os.scandir('.') as entries:
    #     for entry in entries:
    #         if entry.is_file():
    #             print(entry.name)

    # for entry in pathlib.Path('.').iterdir():
    #     print(entry.name)

    
 
    # for file in [item for item in os.scandir('.') if os.path.isfile(item)]:
    #     print(file.name)
    # pass

if __name__ == "__main__":
    main()
