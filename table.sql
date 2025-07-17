CREATE DATABASE if not EXISTS dbrongp;
USE dbrongp;
DROP TABLE if EXISTS action_record;
DROP TABLE if EXISTS physical_condition;
DROP TABLE if EXISTS suspension_control;
DROP TABLE if EXISTS user;

-- userテーブル
CREATE TABLE user (
    user_id INT AUTO_INCREMENT NOT NULL,
    personal_number VARCHAR(10) NOT NULL unique,
    affiliation VARCHAR(30) NOT NULL,
    namae VARCHAR(30) NOT NULL,
    phone_number VARCHAR(20),
    class VARCHAR(10),
    position VARCHAR(10),
    attendance_suspension BOOLEAN DEFAULT FALSE,
    login_pass VARCHAR(20) NOT NULL UNIQUE,
    delflag BOOLEAN DEFAULT FALSE,
    lastupdate DATETIME,
    PRIMARY KEY(user_id)
);

-- action_recordテーブル
CREATE TABLE action_record (
    action_record_id INT AUTO_INCREMENT NOT NULL,
    personal_number VARCHAR(10),
    action_record_date DATE,
    action_record_Time TIME,
    destination VARCHAR(50),
    transportation VARCHAR(50),
    departure VARCHAR(50),
    arrival VARCHAR(50),
    companion BOOLEAN DEFAULT FALSE,
    companion_relationship VARCHAR(50),
    companion_count INT,
    companion_name VARCHAR(50),
    mask_usage VARCHAR(50),
    delflag BOOLEAN DEFAULT FALSE,
    lastupdate DATETIME,

    PRIMARY KEY(action_record_id),
    FOREIGN KEY(personal_number)
	    REFERENCES user(personal_number)
	    ON DELETE CASCADE
	    ON UPDATE CASCADE
);

-- Physical_condition テーブル
CREATE TABLE physical_condition (
    physical_condition_id INT AUTO_INCREMENT NOT NULL,
    personal_number VARCHAR(10),
    condition_date DATE,
    condition_time TIME,
    body_temperature FLOAT,
    joint_muscle_pain BOOLEAN DEFAULT FALSE,
    fatigue BOOLEAN DEFAULT FALSE,
    headache BOOLEAN DEFAULT FALSE,
    sore_throat BOOLEAN DEFAULT FALSE,
    shortness_of_breath BOOLEAN DEFAULT FALSE,
    cough_sneeze BOOLEAN DEFAULT FALSE,
    nausea_vomiting BOOLEAN DEFAULT FALSE,
    abdominal_pain_diarrhea BOOLEAN DEFAULT FALSE,
    taste_disorder BOOLEAN DEFAULT FALSE,
    smell_disorder BOOLEAN DEFAULT FALSE,
    attendance_suspension BOOLEAN DEFAULT FALSE,
    delflag BOOLEAN DEFAULT FALSE,
    lastupdate DATETIME,
    PRIMARY KEY(physical_condition_id),
    FOREIGN KEY(personal_number)
	    REFERENCES user(personal_number)
	    ON DELETE CASCADE
	    ON UPDATE CASCADE
);

-- suspension_controlテーブル
CREATE TABLE suspension_control (
    suspension_control_id INT AUTO_INCREMENT NOT NULL,
    personal_number VARCHAR(10),
    sc_start DATE,
    sc_finish DATE,
    remarks TEXT,
    medical_institution_name VARCHAR(10),
    attending_physician VARCHAR(20),
    delflag BOOLEAN DEFAULT FALSE,
    lastupdate DATETIME,

    PRIMARY KEY(suspension_control_id),
    FOREIGN KEY(personal_number)
	    REFERENCES user(personal_number)
	    ON DELETE CASCADE
	    ON UPDATE CASCADE
);