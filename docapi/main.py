import shutil
from pathlib import Path
from fire import Fire

from docapi.docapi import DocAPI


class Main:
    '''DocAPI is a Python package that automatically generates API documentation using LLM. '''        

    @staticmethod
    def generate(app_path, doc_dir='./docs', lang='zh', config=None):
        '''Generate API documentation.
        Args:
            app_path (str): Path to the API service entry.
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            lang (str, optional): Language of the documentation. Defaults to 'zh'.
            config (str, optional): Path to the configuration file. Defaults to None.
        '''
        docapi = DocAPI.build_flask(lang, config)
        docapi.generate(app_path, doc_dir)

    @staticmethod
    def update(app_path, doc_dir='./docs', lang='zh', config=None):
        '''Update API documentation.
        Args:
            app_path (str): Path to the API service entry.
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            lang (str, optional): Language of the documentation. Defaults to 'zh'.
            config (str, optional): Path to the configuration file. Defaults to None.
        '''
        docapi = DocAPI.build_flask(lang, config)
        try:
            docapi.update(app_path, doc_dir)
        except FileNotFoundError:
            docapi.generate(app_path, doc_dir)

    @staticmethod
    def init(output='./'):
        '''Initialize the configuration file.
        Args:
            output (str, optional): Path to the output directory. Defaults to './'.
        '''
        raw_path = Path(__file__).parent / 'config.yaml'
        shutil.copy(str(raw_path), output)
        print(f'Create config file: {output}')

    @staticmethod
    def serve(doc_dir='./docs'):
        '''Under development.'''

def run():
    return Fire(Main)


if __name__ == '__main__':
    run()
