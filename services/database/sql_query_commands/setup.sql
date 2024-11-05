CREATE TABLE IF NOT EXISTS user(
    email VARCHAR(320) NOT NULL UNIQUE,
    hash_password TEXT NOT NULL,
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    authkey VARCHAR(500) UNIQUE, 
    creation_date TIMESTAMP NOT NULL DEFAULT '2024-11-4 22:00:00', -- main.py updates this value ;)

    -- nullable data
    username VARCHAR(50),
    age SMALLINT,
    gender CHAR,
    github_profile_url VARCHAR(39),

    -- stuff about the subjects that the student/user will interact to
    favorited_courses TEXT, -- Will be a list with the fav-courses id's
    modules_skipped TEXT, -- list with the modules marked as skipped
    modules_inprogress TEXT, -- Modules the student is looking trought
    modules_done TEXT, -- Student's learned modules
    -- those list components will be split with the ',' separator

    -- auto-set-stuff
    user_role CHAR DEFAULT 'S', -- Developer, Teacher, Student and Moderator

    -- Data analyze stuff
    interaction_time BIGINT, -- track the time user spends using the application
    interaction_count BIGINT -- how many interactions the user made
)

CREATE TABLE IF NOT EXISTS logs(
    time_location TIMESTAMP,
    output_message TEXT,
    message_type CHAR DEFAULT 'M', -- M, W, E, C -- Message Warn Error Comment
)