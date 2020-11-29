# [ESUITS](https://github.com/jphacks/D_2014)のデータベースを設計し直してアプリケーションを修正
以前ハッカソンで作成したエントリシート作成支援アプリケーションを作成したが，時間もなくデータベースの設計が割と適当だったのであらためて設計し直して適用したい．

でそのときに苦労したことをここに残す．

 # モデルの再設計
 再設計したデータベースのER図は[ここ](https://github.com/junkhp/esuits_db_check/blob/main/esuits_db_er.pdf)

ポイント
- ユーザーとタグを多対多にした．(以前は一対多)
- エントリーシートのテーブルから企業テーブルと企業URLテーブルを分離

# アプリケーションそのものの修正
モデルの設計は完了したが，それに伴いアプリそのものを修正しないといけないのでそれについてやったことを書く．
大きく変更し，困りそうなのが以下の2点
- 質問の追加(ユーザーテーブルと多対多になってどうなるのか)
- エントリーシートの追加(企業テーブルと企業URLテーブルが分離したことによってどうなるのか)
## 多対多になって質問の追加はどうなるのか
### シチュエーション
- ユーザーを追加するときには，そのユーザーはタグをもっていないから特に気にすることはない(できれば新規ユーザーにも幾つかデフォルトのタグを与えたい)
- 各ユーザーは必要に応じて自分でタグを作成する．

### やったこと
addする！

## 新しくエントリーシートを追加するときはどうしたらいいのか