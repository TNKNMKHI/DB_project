# 📊 データベーステーブル設計一覧

## 🧑‍💼 `user` テーブル（ユーザー情報）

| フィールド名           | 型             | 説明                       |
|------------------------|----------------|----------------------------|
| user_id               | INT            | 主キー／AUTO_INCREMENT     |
| personal_number       | VARCHAR(10)    | 学籍番号または個人番号     |
| affiliation           | VARCHAR(30)    | 学科・部課室               |
| namae                 | VARCHAR(30)    | 氏名                       |
| phone_number          | VARCHAR(20)    | 電話番号                   |
| class                 | VARCHAR(10)    | 所属（学生・教員など）     |
| position              | VARCHAR(10)    | 役職                       |
| attendance_suspension | BOOLEAN        | 出席停止フラグ             |
| login_pass            | VARCHAR(20)    | ログインパスワード（UNIQUE）|
| delflag               | BOOLEAN        | 削除フラグ                 |
| lastupdate            | DATETIME       | 最終更新日                 |

---

## 🗺️ `Action` テーブル（行動記録）

| フィールド名            | 型            | 説明                       |
|-------------------------|---------------|----------------------------|
| Action_id              | INT           | 主キー／AUTO_INCREMENT     |
| user_id                | INT           | 外部キー（user）           |
| Action_date            | DATE          | 日付                       |
| Action_Time            | TIME          | 時間                       |
| Destination            | VARCHAR(50)   | 行先                       |
| Transportation         | VARCHAR(50)   | 移動方法                   |
| Departure              | VARCHAR(50)   | 出発地                     |
| arrival                | VARCHAR(50)   | 到着地                     |
| Companion              | BOOLEAN       | 同行者の有無               |
| companion_relationship | VARCHAR(50)   | 同行者との関係             |
| companion_count        | VARCHAR(50)   | 同行者の人数               |
| Companion_name         | VARCHAR(50)   | 同行者名                   |
| mask_usage             | VARCHAR(50)   | マスク使用状況             |
| delflag                | BOOLEAN       | 削除フラグ                 |
| latupdate              | DATETIME      | 最終更新日                 |

---

## 🌡️ `Physical_condition` テーブル（体調観察）

| フィールド名               | 型            | 説明                        |
|----------------------------|---------------|-----------------------------|
| Physical_condition_id      | INT           | 主キー／AUTO_INCREMENT      |
| user_id                    | INT           | 外部キー（user）            |
| Condition_Date             | DATE          | 観察日                      |
| condition_Time             | TIME          | 時間帯（AM／PM）            |
| body_temperature           | FLOAT         | 体温                        |
| joint_muscle_pain          | BOOLEAN       | 関節・筋肉痛                |
| fatigue                    | BOOLEAN       | だるさ                      |
| headache                   | BOOLEAN       | 頭痛                        |
| sore_throat                | BOOLEAN       | 喉の痛み                    |
| shortness_of_breath        | BOOLEAN       | 息苦しさ                    |
| cough_sneeze               | BOOLEAN       | 咳・くしゃみ                |
| nausea_vomiting            | BOOLEAN       | 吐気・嘔吐                  |
| abdominal_pain_diarrhea    | BOOLEAN       | 腹痛・下痢                  |
| taste_disorder             | BOOLEAN       | 味覚障害                    |
| smell_disorder             | BOOLEAN       | 嗅覚障害                    |
| attendance_suspension      | BOOLEAN       | 出席停止                    |
| Suspension_control_id      | INT           | 外部キー（Suspension_control）|
| delflag                    | BOOLEAN       | 削除フラグ                  |
| latupdate                  | DATETIME      | 最終更新日                  |

---

## ⛔ `Suspension_control` テーブル（出席停止管理）

| フィールド名               | 型            | 説明                        |
|----------------------------|---------------|-----------------------------|
| Suspension_control_id      | INT           | 主キー／AUTO_INCREMENT      |
| user_id                    | INT           | 外部キー（user）            |
| Start                      | DATE          | 開始日                      |
| finish                     | DATE          | 終了予定日                  |
| remarks                    | TEXT          | 備考                        |
| medical_institution_name   | VARCHAR(10)   | 医療機関名                  |
| attending_physician        | VARCHAR(20)   | 医師名                      |
| delflag                    | BOOLEAN       | 削除フラグ                  |
| latupdate                  | DATETIME      | 最終更新日                  |

