import os, argparse, yaml, logging

def read_params(config_path:str):
    try:
        with open(config_path) as yaml_file:
            config = yaml.safe_load(yaml_file)
        return config
    except Exception as e:
        print(e)

def main(config_path:str, datasource:str):
    try:
        config = read_params(config_path)
        print(config)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    default_config_path = os.path.join('config', 'params.yaml')
    args.add_argument('--config', default=default_config_path)
    args.add_argument('--datasource', default=None)

    parsed_args = args.parse_args()

    main(config_path= parsed_args.config, datasource= parsed_args.datasource)
    