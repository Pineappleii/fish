## 使用说明

##### 新建.env

##### 构建fish-base

docker build -f Dockerfile-base -t fish-base .

##### 构建fish

docker build -t fish .

##### 启动fish

docker run -d -p 80:80 --name fish