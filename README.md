# 爬虫练习站点 —— 部署与使用说明

> 本目录是《Python程序设计》第11章"网络爬虫"课程的**教学用静态测试站点**，
> 与 `11学生实验手册_网络爬虫_3课时.py` 完全配套。
> 所有内容均为虚构示例，不涉及真实个人信息或商业数据，可放心供学生练习爬取。

---

## 一、目录结构

```
爬虫练习站点/
├── index.html            ← 首页（新闻列表 + 颜色列表 + 表格 + 图片 + 链接）
├── news/
│   ├── news1.html        ← 新闻详情页一（开学典礼）
│   ├── news2.html        ← 新闻详情页二（阅读推广）
│   └── news3.html        ← 新闻详情页三（运动会）
├── images/
│   ├── campus1.png       ← 占位图片（纯色+文字，可被下载）
│   ├── campus2.png
│   └── campus3.png
└── README.md             ← 本说明文件
```

## 二、如何部署到自己的域名

这是**纯静态站点**，任意一种方式都能跑：

1. **GitHub Pages / Gitee Pages**：把 `爬虫练习站点` 里的内容推到仓库根目录（或 `docs/`），开启 Pages 即可。
2. **自有服务器（Nginx/Apache）**：把目录内容放到站点根目录，如 `/var/www/html/`。
3. **本地快速测试**：直接双击 `index.html`，或用 `python -m http.server` 启动。
   ```bash
   cd 爬虫练习站点
   python -m http.server 8000
   # 浏览器访问 http://127.0.0.1:8000/
   ```

> 部署后，把根网址（例如 `https://你的域名/`）告诉学生，替换实验手册里
> 那些已失效的第三方演示地址（如 `www.musi-cal.com`、`mp.weixin.qq.com` 等）。

## 三、每个页面 / 元素对应的实验手册练习点

| 练习点 | 位置 | 对应手册实验 | 可练技能 |
|--------|------|------------|---------|
| HTML 标签认识 | 首页各类标签 | 实验1 | h/p/a/img/table/ul/li/div |
| 新闻列表链接 | 首页 `class="c75870"` 的 a 标签 | 实验9 | XPath 提取标题+链接 |
| 颜色列表 | 首页 `ul id="colors"` | 实验1、11 | select('#colors li') |
| 图书表格 | 首页 `table` | 实验1 | 提取 tr/td 表格数据 |
| 图片地址 | 首页 `data-src`、详情页 `img` | 实验5、6、14 | 正则提取+下载图片 |
| 友情链接 | 首页 `#links` 列表 | 实验13 | 提取 http 开头的外链 |
| 新闻标题 | 详情页 `h1` | 实验9 | `//h1//text()` |
| 新闻正文 | 详情页 `div id="vsb_content"` | 实验9 | `//div[@id="vsb_content"]` |
| 图片保存 | 详情页正文内的 `img` | 实验9 | `each_picture` 回调 |
| GET/POST | 见下方"参数练习" | 实验4 | urlencode / data 提交 |

## 四、GET / POST 参数练习

手册实验4里教材用的 `www.musi-cal.com`、`requestb.in` 等地址早已失效。
本静态站点无法直接"回显" POST 参数（需要后端脚本），课堂可选以下替代方案：

### 方案A（推荐，零后端）：用公开测试接口
```python
import requests
# GET：参数自动编码到 URL
r = requests.get('https://httpbin.org/get', params={'spam':1, 'eggs':2, 'bacon':0})
print(r.json()['args'])

# POST：data 提交表单
r = requests.post('https://httpbin.org/post', data={'key1':'value1', 'key2':'value2'})
print(r.json()['form'])
```
> `httpbin.org` 是专门用于 HTTP 请求测试的公开服务，返回内容一目了然，非常适合教学。

### 方案B（自建回显接口）：给站点加一个 CGI/PHP 脚本
如果希望学生把请求发到**自己的域名**，可加一个简单回显脚本。例如用 Python 的 CGI：

在服务器 cgi-bin 目录放 `echo.py`（内容见 `api/echo.py` 示例），学生访问
`https://你的域名/cgi-bin/echo.py?spam=1&eggs=2` 即可看到回显的 GET 参数。

## 五、课堂使用建议

1. 先让学生用浏览器打开站点、右键"查看网页源代码"，对照实验1认识标签。
2. 用 `urllib.request.urlopen` 抓取首页（实验3），观察 bytes 与 decode。
3. 用正则/BeautifulSoup 提取颜色列表、图书表格、图片地址（实验5、6、13）。
4. 用 Scrapy 复刻实验9：`parse` 抓首页列表 → `each_page` 抓详情 → `each_picture` 存图。
   （只需把手册里 `start_urls` 改成你自己的域名即可）

## 六、合规说明

本站点是教学演示用的自建页面，内容虚构，可放心让学生练习；
若学生去爬**真实网站**，请务必遵守网站 robots 协议、授权要求及相关法律法规。
