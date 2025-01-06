CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
);

CREATE TABLE profiles (
    profile_id INT PRIMARY KEY,
    username TEXT UNIQUE,
    nickname TEXT,
    hobbies TEXT,
    interests TEXT,
    fav_color TEXT,
    fav_food TEXT,
    fav_movie TEXT,
    FOREIGN KEY (profile_id) REFERENCES users(id)
);