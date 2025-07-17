# 📊 データベーステーブル設計一覧（改訂版）

## 🧑‍💼 `user` テーブル（ユーザー情報）

| フィールド名           | 型             | 説明                       |
|------------------------|----------------|----------------------------|
| user_id               | INT            | 主キー／AUTO_INCREMENT     |
| personal_number       | VARCHAR(10)     | 学籍番号・個人番号（UNIQUE）|
| affiliation           | VARCHAR(30)     | 学科・部課室               |
| namae                 | VARCHAR(30)     | 氏名                       |
| phone_number          | VARCHAR(20)     | 電話番号                   |
| user_class                 | VARCHAR(10)     | 所属（学生・教員など）     |
| position              | VARCHAR(10)     | 役職                       |
| attendance_suspension | BOOLEAN         | 出席停止フラグ             |
| delflag               | BOOLEAN         | 削除フラグ                 |
| lastupdate            | DATETIME        | 最終更新日                 |

---
## 🧑‍💼 `user_auth` テーブル（パスワード情報）
| フィールド名           | 型             | 説明                       |
|------------------------|----------------|----------------------------|
auth_id            | INT            | 主キー／AUTO_INCREMENT     |
personal_number           | INT            | 外部キー（user.personal_number）   | AUTO_INCREMENT PRIMARY KEY,UNIQUE
password_hash       | VARCHAR(255)| NOT NULL,
salt| VARCHAR(32)| NOT NULL,
| last_update        | DATETIME       | 最終更新日                 |
| delflag            | BOOLEAN        | 削除フラグ                 |
---

## 🗺️ `action_record` テーブル（行動記録）

| フィールド名            | 型            | 説明                       |
|-------------------------|---------------|----------------------------|
| action_record_id       | INT           | 主キー／AUTO_INCREMENT     |
| personal_number        | INT           | 外部キー（user.personal_number）|
| action_record_date     | DATE          | 行動日                     |
| action_record_time     | TIME          | 行動時間                   |
| destination            | VARCHAR(50)   | 行先                       |
| transportation         | VARCHAR(50)   | 移動方法                   |
| departure              | VARCHAR(50)   | 出発地                     |
| arrival                | VARCHAR(50)   | 到着地                     |
| companion              | BOOLEAN       | 同行者の有無               |
| companion_relationship | VARCHAR(50)   | 同行者との関係             |
| companion_count        | INT           | 同行者の人数               |
| companion_name         | VARCHAR(50)   | 同行者名                   |
| mask_usage             | VARCHAR(50)   | マスク使用状況             |
| delflag                | BOOLEAN       | 削除フラグ                 |
| latupdate              | DATETIME      | 最終更新日                 |

---

## 🌡️ `physical_condition` テーブル（体調観察）

| フィールド名               | 型            | 説明                        |
|----------------------------|---------------|-----------------------------|
| physical_condition_id      | INT           | 主キー／AUTO_INCREMENT      |
| personal_number            | INT           | 外部キー（user.personal_number）|
| condition_date             | DATE          | 観察日                      |
| condition_time             | TIME          | 時間帯（AM／PM）            |
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
| attendance_suspension      | BOOLEAN       | 出席停止フラグ              |
| delflag                    | BOOLEAN       | 削除フラグ                  |
| latupdate                  | DATETIME      | 最終更新日                  |

---

## ⛔ `suspension_control` テーブル（出席停止管理）

| フィールド名               | 型            | 説明                        |
|----------------------------|---------------|-----------------------------|
| suspension_control_id      | INT           | 主キー／AUTO_INCREMENT      |
| personal_number            | INT           | 外部キー（user.personal_number）|
| sc_start                   | DATE          | 出席停止開始日              |
| sc_finish                  | DATE          | 出席停止終了予定日          |
| remarks                    | TEXT          | 備考                        |
| medical_institution_name   | VARCHAR(10)   | 医療機関名                  |
| attending_physician        | VARCHAR(20)   | 医師名                      |
| delflag                    | BOOLEAN       | 削除フラグ                  |
| latupdate                  | DATETIME      | 最終更新日                  |
