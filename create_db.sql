CREATE TABLE Files (
    FileID INTEGER NOT NULL PRIMARY KEY,
    File1 BLOB NOT NULL,
    File2 BLOB,
    File3 BLOB,
    File4 BLOB,
    File5 BLOB,
    File6 BLOB,
    File7 BLOB,
    File8 BLOB,
    File9 BLOB,
    File10 BLOB
    );

CREATE TABLE Categories (
    CatID INTEGER NOT NULL PRIMARY KEY,
    Name varchar(255) NOT NULL
);

CREATE TABLE Collection (
    ColID INTEGER NOT NULL PRIMARY KEY,
    FileID INT NOT NULL,
    CatID INT NOT NULL,
    Name_desc varchar(255) NOT NULL,
    Tags varchar(1047) NOT NULL,
    FOREIGN KEY (FileID) REFERENCES Files(FileID),
    FOREIGN KEY (CatID) REFERENCES Categories(CatID)
);
