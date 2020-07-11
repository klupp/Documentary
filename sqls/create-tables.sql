CREATE TABLE pages (
    pageId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    format TEXT,
    pageNum INTEGER,
    CHECK (format IN ('A4'))
);

CREATE TABLE layers (
    layerId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    format TEXT,
    ref TEXT,
    CHECK (format IN ('A4'))
);

CREATE TABLE pageLayerMap (
    pageId INTEGER NOT NULL,
    layerId INTEGER NOT NULL,
    layerOrder INTEGER,
    PRIMARY KEY (pageId, layerId),
    UNIQUE (pageId, layerId, layerOrder),
    FOREIGN KEY (pageId) REFERENCES pages(pageId),
    FOREIGN KEY (layerId) REFERENCES pages(layerId)
);

CREATE TABLE dataSources (
    sourceId INTEGER not NULL PRIMARY KEY AUTOINCREMENT,
    sourcePath TEXT UNIQUE,
    projectPath TEXT UNIQUE,
    name TEXT UNIQUE,
    format TEXT,
    CHECK (format IN ('csv'))
);