![image](assets/logo.png)

![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![OS](https://img.shields.io/badge/os-linux%20|%20macOS-blue)
![Lisence](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)

\[ English | [中文](README_zh.md) \]

DocAPI is a Python package that uses LLM to automatically generate API documentation.

## Features

- The Flask framework supports automatic scanning of the routing structure of API services;

- Supports Tongyi Qianwen, OpenAI, Azure OpenAI, open source models, etc;

- Supports automatic document generation and partial document update;

- Support Chinese and English documents;

- Supports web page deployment to display API documentation.

## Installation

```bash
pip install docapi
```

or

```bash
pip install -U docapi -i https://pypi.org/simple
```

#### GitHub source code installation

```bash
pip install git+https://github.com/Shulin-Zhang/docapi
```

## Usage

#### Method 1 (Recommended)

**Automatically scan the routing structure. This is only valid for flask projects and must be used in the environment of api projects.**

```bash
export OPENAI_API_KEY=your_key

# Generate API documentation
docapi generate server.py

# Update API documentation
docapi update server.py

# Start the web service
docapi serve
```

or

```bash
export OPENAI_API_KEY=your_key

export OPENAI_API_BASE=api_base_url

export OPENAI_API_MODEL=model_name

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动web服务
docapi serve
```

#### Method 2

Generate the configuration file

```bash
docapi init
```

Edit the config.yaml file

```yaml
# API file list

api_files: 
  - 'flask_server.py'
  - 'flask_api.py'

# OpenAI

openai_api_key: xxx

openai_base_url: 'http://ip:port/v1'

openai_model: 'qwen-plus'

# Azure OpenAI

azure_api_key: null

azure_endpoint: null

azure_api_version: null

azure_model: null
```

```bash
# Generate API documentation
docapi generate --doc_dir ./docs --lang zh --config config.yaml

# Update API documentation
docapi update --doc_dir ./docs --lang zh --config config.yaml

# Start the web service
docapi serve ./docs -h 127.0.0.1 -p 9000
```

## Supported Models

- OpenAI

- AzureOpenAI

- Tongyi Qianwen

## Supported API Frameworks

- Flask
  
Automatic scanning is only valid for the Flask framework and is recommended for use on Flask services.

## API Web Page

![image](assets/example1.png)

## TODO

- Supports large models such as Wenxin Yiyan and Zhipu AI.

- Supports automatic scanning of frameworks such as fastapi and Django.

- ~~Supports online web page display of documents.~~

- Supports custom document templates.

- Multithreading accelerates requests.

- Import to postman.
