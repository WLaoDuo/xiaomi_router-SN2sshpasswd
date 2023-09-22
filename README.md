手动写snort规则偶尔出错，想对于简单的get，post包过滤写个自动生成工具

metadata:service http;

content:"GET";http_method;
content:"POST";http_method;

content:"/xxxx/url";http_uri;

content:"";http_client_body;

flow:to_server;established;

offset左起偏移量:2; depth搜索长度:2;
