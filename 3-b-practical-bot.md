# 3-b. LINE Messaging API を利用した本格Botの開発 (後半)

## Pico Wとの連携

せっかく手元にPico Wがあるので，今の温度を教えてくれるBotを作ってみます．

本来であれば

1. ユーザーが送信したLINEメッセージをトリガーとしてPico Wに送信し，
1. Pico Wが温度を計測してユーザーに送信する

とよいのですが，諸々の事情から今回は

1. Pico Wが定期的に温度をスプレッドシートに記録し，
1. ユーザーからリクエストがあったとき，最新の値を送信する

システムをつくります．

### 1. Pico Wが計測した温度をスプレッドシートに記録する

#### スプレッドシートのセットアップ

1. LINE Botが使用するスプレッドシートとは別に，Pico Wが記録するスプレッドシートを作成します．  
[Google Drive](https://drive.google.com/)にアクセスし，任意の場所で左上の`新規`→`スプレッドシート`をクリックします．

1. 先ほど作成したスプレッドシートと混合しないようにするために  
左上の`無題のスプレッドシート`をクリックして名前を`Pico W`に変更しておきます．

1. 上部の`拡張機能`から`Apps Script`を開き，書きかけの`myFunction`関数を削除して以下のコードに置き換えます．
    ```js
    function doPost(e){
        let sheet = SpreadsheetApp.getActive().getActiveSheet();
        sheet.appendRow([new Date(), e.postData.contents]);
    }
    ```

1. 左上の`無題のプロジェクト`をクリックして名前を`Pico W`に変更しておきます．

1. 右上の`デプロイ`→`新しいデプロイ`をクリックし，`種類を選択`の右にある`歯車⚙`から`ウェブアプリ`を選択します．

1. 表示された設定のうち，`アクセスできるユーザー`を`全員`に変更し，`デプロイ`をクリックします．

1. `アクセスを承認`をクリックし，ご自身のGoogleアカウントを選択します．  
`Google hasn't verified this app`と表示されますが，左下に小さく表示された`Advanced`から  
`Go to Pico W(unsafe)`をクリックします．

1. スプレッドシートの編集などを求める権限リクエストが表示されますので，`Allow`をクリックして許可します．

1. 問題なければ，デプロイIDとウェブアプリのURLが発行されます．  
このうち`ウェブアプリのURL`をコピーして，メモ帳などのアプリケーションに記録しておきます．

1. Windowsの方はコマンドプロンプト(Win+R→`cmd`→Enter)またはWSL上のBash，Macの方はターミナル.appで以下のコマンドを実行します．  
PowerShellでは`curl`を`curl.exe`とする必要があります．
    ```sh
    curl -X POST -H "Accept: application/json" -H "Content-type: application/json" -d "テストメッセージ" ウェブアプリのURL
    ```

実行後，
```html
<!DOCTYPE html><html>〜スクリプトが完了しましたが、何も返されませんでした。〜</html>
```
と出力されますが，スプレッドシートに正しく情報を記録できていればOKです．

#### Pico Wのセットアップ

1. Thonnyを開いて，Pico Wへ以下のコードを書き込んでください．
    ```python
    (TBD)
    ```

実行後，スプレッドシートに値が記録されていればOKです．

### 2. ユーザーのリクエストに応じて最新の温度を送信する

[前半](3-a-practical-bot.md)の制作物を活用して実装します．  
あえて説明を減らしています．よくわからない箇所は検索や周囲の人に頼りながらやってみましょう．

1. 前半で作成した`LINE Bot`というタイトルのスプレッドシート・Google Apps Scriptプロジェクトを開きます．

1. `doPost`関数に，以下のように実装します．
    - ユーザから`教えて`というテキストメッセージが送信されたら，  
    `Pico W`シートに記録された温度の値を返信する
        <details><summary>💡ヒント</summary>

        1. 予めPico WのシートからLINEシートの特定の位置に，スプレッドシートの[IMPORTRANGE関数](https://excel-ubara.com/spreadsheet1/spreadsheet051.html)を利用してデータを取り込んでおく  
        // GAS単体でも[実現できます](https://excel-ubara.com/apps_script1/GAS015.html)  

        2. `// TBD`の箇所に，上記関数で取り込んだセルの内容を送信する  
        参考：[Google Apps Script と LINEを使ったオウム返しBotの作成方法](https://note.com/haru_maki_ch/n/n18785eab4900)
        </details>

    - その他のテキストメッセージや，テキストでないメッセージが送信されたら，  
    このBotの使い方を教えるメッセージを返信する

## Botのカスタマイズ

ここまでできたら，ぜひLINE Developersのコンソール画面やLINE Official Account Managerをいろいろ触ってみてください．  
友達登録後に自動でメッセージを送信したり，ご自身で開発するWebアプリケーションにLINEログインの機能を追加したりすることが簡単にできます．  

APIの扱いに慣れている人は，[Messaging APIリファレンス](https://developers.line.biz/ja/reference/messaging-api/) を参照してより高度なBotの開発に挑戦してみましょう．  
グループトークで活躍できるBotを作ったり，企業の公式LINEでよくあるリッチメニューやボタンを作ったりすることだってできます．

[Chat GPTなどの生成系AIと連携させる](https://zenn.dev/robes/articles/c8dda8b42afab8)ことでより簡単に高機能なBotを作れるかもしれません．ぜひいろいろと試してみましょう！  
困ったときは遠慮なく近くのCore-team Memberにお声掛けくださいね．

[目次に戻る](README.md)