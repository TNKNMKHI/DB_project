### テーブル設計

#### personテーブル
|名前|型|属性|備考|
|---|--|--|--|
|personID|int|primary key <br> auto increment| -- |
|personcode|int|--|外部用ID
|name|VARCHAR(30)|--|名前
|zipcode|VARCHAR(8)|--|郵便番号
|prefecture|VARCHAR(4)|--|都道府県
|city|VARCHAR(6)|--|市町村
|address1|VARCHAR(10)||住所1
|address2|VARCHAR(10)||住所2

#### studentテーブル
|名前|型|属性|備考|
|---|--|--|--|
|studentID|int|primary key <br> auto increment| -- |
|personcode|int|--|外部用ID
|studentcode|int|--|学籍番号

#### teacherテーブル
|名前|型|属性|備考|
|---|--|--|--|
|teacherID|int|primary key <br> auto increment| -- |
|personcode|int|--|外部用ID
|teachercode|int|--|先生コード
|type|VARCHAR(5)|--|先生のタイプ

#### 職員テーブル
|名前|型|属性|備考|
|---|--|--|--|
|officerID|int|primary key <br> auto increment| -- |
|personcode|int|--|外部用ID
|officerrcode|int|--|職員コード
|type|VARCHAR(5)|--|職員のタイプ

#### 行動テーブル
|名前|型|属性|備考|
|---|--|--|--|



