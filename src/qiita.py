import http.client
import json

# 表示するユーザ名


def get_items(user_id: str, item_num: int = 10, page: str = "1", par_page: str = "100"):

    conn = http.client.HTTPSConnection("qiita.com", 443)
    conn.request(
        "GET", f"/api/v2/users/{user_id}/items?page={page}&per_page={par_page}")
    res = conn.getresponse()
    print(res.status, res.reason)
    data = res.read().decode("utf-8")

    # 文字列からJSON オブジェクトへでコード
    jsonstr = json.loads(data)

    print("==========================================================")
    # ヘッダ出力
    print("\"no\",\"created_at\",\"tile\",\"url\"")

    # 投稿数を指定
    for num in range(item_num):
        created_at = jsonstr[num]['created_at']
        tile = jsonstr[num]['title']
        url = jsonstr[num]['url']

        # ダブルクォートありCSV形式で出力
        print("\"" + str(num) + "\",\"" + created_at +
              "\",\"" + tile + "\",\"" + url + "\"")

    print("==========================================================")
    conn.close()
