# 3-a. LINE Messaging API を利用した本格Botの開発 (前半)

Google Apps Script(GAS)を用いて，より本格的な機能を利用できるLINE Botを作成します．

> [!NOTE]  
> このハンズオンでは，Messaging APIの無料枠の中で実装します．   
> ご自身で独自に実装を拡張される場合，Botからの自発的なメッセージは500通/月を超えると費用が発生しますのでご注意ください．  
> ただし，支払い手続きを行う前に課金されることはありません．  
> 詳しくは[こちら](https://www.lycbiz.com/jp/service/line-official-account/plan/)をご覧ください．  

## LINE Developersアカウントの作成

まずは [LINE Developers](https://developers.line.biz/ja/) のサイトにアクセスし，右上の`コンソールにログイン`をクリックします．

開いた画面で`LINEアカウントでログイン`をクリックし，ご自身のLINEアカウントでログインされてください．

> [!TIP]
> QRコードログイン機能が便利です．

ログインできたら，まずはプロバイダー(Bot開発者のプロフィール)を作成します．  
プロバイダー画面で，`作成`をクリックして手順に従い作成します．

## Messaging API利用のための初期設定

1. チャネル設定画面より，Messaging APIを有効化します．
`Messaging API`の画像をクリックします．

1. 以下の項目をそれぞれ入力・アップロードし，利用規約を確認して`作成`をクリックします．
    - 会社・事業者の所在地・地域：日本
    - チャネルアイコン：任意
    - チャネル名：Botの名前を決めてください
    - チャネル説明
    - 大業種：保育・学校
    - 大学所属サークル・部活動

1. `以下の内容でMessaging APIチャネルを作成しますか？`と表示されます．内容を確認して，問題なければ`OK`をクリックします．

1. `チャネル基本設定`を下にスクロールし，以下の要素をコピーしてメモ帳などのアプリケーションに控えておきます．
    - チャネルID
    - チャネルシークレット(発行を押すと再発行されます)

1. `Messaging API設定`を開き，表示されたQRコードをお手持ちのスマートフォンでスキャンして友だちとして登録します．

1. `Messaging API設定`の最下部にスクロールして`チャネルアクセストークン(長期)`の`発行`をクリックします．  
表示されたチャネルアクセストークンは，チャネルシークレットと同様に控えておきます．

1. これからGoogle Apps Scriptを使用しますが，その後このLINE Developersのコンソール画面を再び操作します．  
閉じないようにしておきましょう．

> [!CAUTION]
> チャネルシークレットやチャネルアクセストークンは，他者に知られないように注意してください．  
> もしGitHubの公開リポジトリなどでうっかり公開してしまったときは，速やかに`発行`ボタンをクリックして以前のものを無効化します．

## Google Apps Scriptを書いてみる

これからGoogle Apps Scriptを使って，サーバプログラムを書いていきます．  
まずはLINE Botから正常に情報を取得できるか試してみます．

1. [Google Drive](https://drive.google.com/)にアクセスし，任意の場所で左上の`新規`→`スプレッドシート`をクリックします．

1. 後からもう1つスプレッドシートを作成します．分かりやすくするために  
左上の`無題のスプレッドシート`をクリックして名前を`LINE Bot`に変更しておきます．

1. 上部の`拡張機能`から`Apps Script`を開きます．

1. 同様に左上の`無題のプロジェクト`をクリックして名前を`LINE Bot`に変更しておきます．

1. 書きかけの`myFunction`関数がありますがこれを削除して，以下のコードに置き換えます．
    ```
    function doPost(e){
        let sheet = SpreadsheetApp.getActive().getActiveSheet();
        sheet.appendRow([new Date(), e.postData.contents]);
    }
    ```

1. 右上の`デプロイ`→`新しいデプロイ`をクリックし，`種類を選択`の右にある`歯車⚙`から`ウェブアプリ`を選択します．

1. 表示された設定のうち，`アクセスできるユーザー`を`全員`に変更し，`デプロイ`をクリックします．

1. `アクセスを承認`をクリックし，ご自身のGoogleアカウントを選択します．  
このとき，Googleが承認していない開発者によるアプリケーションを実行しようとしているため   
`Google hasn't verified this app`と表示されます．  自身で作成したアプリですので承認します．  
左下に小さく表示された`Advanced`から`Go to LINE Bot(unsafe)`をクリックします．

1. スプレッドシートの編集などを求める権限リクエストが表示されますので，`Allow`をクリックして許可します．

1. 問題なければ，デプロイIDとウェブアプリのURLが発行されます．  
このうち`ウェブアプリのURL`をコピーして，メモ帳などのアプリケーションに記録しておきます．

## Webhook URLの設定

1. LINE Developersのコンソール画面を開き，`Messaging API設定`からWebhook URLの`編集`ボタンをクリックします．

1. 先ほど生成したウェブアプリのURLをここにペーストし，`更新`をクリックします．

1. `Webhookの利用`をオンにして，`Webhook URL`の`検証`をクリックします．  
LINE Developersのコンソール画面に`成功`と表示され，元のGoogleスプレッドシートに以下のような文字列が記録されればOKです．
    ```
    2024/04/16 15:00:00 {"destination":"U3a4...","events":[]}
    ```

1. `LINE公式アカウント機能`の`応答メッセージ`の右にある`編集`をクリックし，`応答メッセージ`をオフにします．

1. LINEアプリから作成したBotアカウントに対して，何らかのメッセージを送信してみます．  
Googleスプレッドシートに以下のような文字列が記録されればOKです．
    ```
    2024/04/16 15:20:00	{"destination":"U3a4...","events":[{"type":"message","message":{"type":"text","id":"5040...","quoteToken":"vFKAy...","text":"送信した文字列"},"webhookEventId":"01HV...","deliveryContext":{"isRedelivery":false},"timestamp":1713...,"source":{"type":"user","userId":"U97c..."},"replyToken":"ed08...","mode":"active"}]}
    ```

    少し読みにくいので整形すると，以下のようなJSON形式のメッセージが出力されたことを確認できます．  
    今回は[こちらのWebサービス](https://rakko.tools/tools/63/)を使って整形しました．

    ```
    {
        "destination": "U3a4...",
        "events": [
            {
                "type": "message",
                "message": {
                    "type": "text",
                    "id": "5040...",
                    "quoteToken": "vFKAy...",
                    "text": "送信した文字列"
                },
                "webhookEventId": "01HV...",
                "deliveryContext": {
                    "isRedelivery": false
                },
                "timestamp": 1713...,
                "source": {
                    "type": "user",
                    "userId": "U97c..."
                },
                "replyToken": "ed08...",
                "mode": "active"
            }
        ]
    }
    ```
    どうやら`e.postData.contents`をJSONフォーマットのテキストとして読み込んだとき，  
    送信したメッセージは内部の`events`に含まれる`message.text`に格納されているようですね．

## メッセージ内容の取得

取得したデータのうち，メッセージテキストのみを記録するようにしてみましょう．

1. Google Apps Scriptの編集画面を開きます．

1. 以下の行を見つけ，
    ```
    sheet.appendRow([new Date(), e.postData.contents]);
    ```  
    `e.postData.contents`を`JSON.parse(e.postData.contents).events[0].message.text`に差し替えます．

1. 左上の`デプロイ`→`デプロイを管理`→右上の`鉛筆マーク`をクリックし，
`バージョン`を`新バージョン`にして`デプロイ`をクリックします．

1. 以降，LINEアカウントにテキストメッセージを送ったとき，自分が送信したメッセージ(と日付)のみがスプレッドシートに記録されていればOKです．

それでは，実際に送信されたメッセージを使用した処理を書いていきます．

## メッセージ内容に応じた処理の分岐

送信されたメッセージを解析して，どのような処理を行うか分岐できるようにします．

1. 先ほどの変更により，コードの3行目がとても長く読みにくいコードになっていると思います．  
これは美しくないので，以下のように書き換えます．
    ```
    function doPost(e){
        let sheet = SpreadsheetApp.getActive().getActiveSheet();
        let data = JSON.parse(e.postData.contents);
        let events = data.events;
        
        for(let i = 0; i < events.length; i++){
            let event = events[i];

            if (event.type == 'message'){
                if (event.message.type == 'text'){
                    sheet.appendRow([new Date(), event.message.text]);
                    if (event.message.text == '教えて'){
                        // TBD
                    }
                }
            }
        }
    }
    ```

1. 左上の`デプロイ`→`デプロイを管理`→右上の`鉛筆マーク`をクリックし，
`バージョン`を`新バージョン`にして`デプロイ`．  
LINEアカウントにメッセージを送ってスプレッドシートに記録されることを確認します．  

これで，
- ユーザが送信したメッセージがテキストなのかどうか  
(ほかには，[スタンプや画像などが送信される](https://developers.line.biz/ja/reference/messaging-api/#text-message)場合があります)
- 送信された文字列が規定の文字列と一致するか

などを判定できるようになりました．  
後半では，Raspberry Pi Pico Wと連携したLINE Botの開発に挑戦します．

プログラミング経験のある方は，あとの説明がなくとも好きなように実装できるかもしれません．  
そのまま作成いただいても，後半をskipして応用コンテンツに取り組まれても構いません．

[目次に戻る](README.md)