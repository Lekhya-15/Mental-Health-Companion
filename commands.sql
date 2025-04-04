CREATE TABLE users (
    email VARCHAR(255) PRIMARY KEY,         -- Email as the unique identifier
       password VARCHAR(255) NOT NULL,    -- Hashed password for security
        last_login TIMESTAMP DEFAULT NULL,      -- Stores last login time
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
         updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO users (email, password, last_login, created_at,updated_at)
VALUES ('vachansiddharth3@gmail.com', 'vachan@1', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

CREATE TABLE user_journals (
    journal_id INT PRIMARY KEY AUTO_INCREMENT,  
    email VARCHAR(255) NOT NULL,                 
    journal_text TEXT NOT NULL,                 
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
 journal_date DATE NOT NULL,                  
     FOREIGN KEY (email) REFERENCES users(email) ON DELETE CASCADE 
    );



delete from user_chats;
ALTER TABLE user_chats ADD COLUMN role VARCHAR(255) NOT NULL;

DROP TABLE IF EXISTS user_chats;
CREATE TABLE user_chats (
      chat_id INT PRIMARY KEY AUTO_INCREMENT,    
     email VARCHAR(255) NOT NULL,               
     message TEXT NOT NULL,                     
     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
     role VARCHAR(255) NOT NULL,
     FOREIGN KEY (email) REFERENCES users(email) ON DELETE CASCADE
);

CREATE TABLE mood_tracker (
      mood_id INT PRIMARY KEY AUTO_INCREMENT,  
       email VARCHAR(255) NOT NULL,             
         mood VARCHAR(50) NOT NULL,               
        mood_note TEXT,                          
        submitted_at DATE NOT NULL,              
       CONSTRAINT unique_mood_per_day UNIQUE (email, submitted_at),  
         FOREIGN KEY (email) REFERENCES users(email) ON DELETE CASCADE
);

