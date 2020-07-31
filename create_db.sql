USE master;
GO

CREATE DATABASE PriceAid;
GO

Use PriceAid;
GO

CREATE TABLE [dbo].[administrator](
    [userID] [int] IDENTITY(1,1) NOT NULL PRIMARY KEY,
    [loginStatus] [binary] NOT NULL,
	[email] [nvarchar](255) NOT NULL,
    [password] [nvarchar](255) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[phonenumber] [nvarchar](255) NOT NULL,
);
GO 

CREATE TABLE [dbo].[saved_table](
    [userID] [int],
    [itemID] [int] NOT NULL IDENTITY(1,1) PRIMARY KEY,
    [url] [nvarchar](255) NOT NULL,
	[email] [nvarchar](255) NOT NULL,
	[price] [nvarchar](255) NOT NULL,
	[company_name] [nvarchar](255) NOT NULL,
    CONSTRAINT [FK_tbladministrator_tblsaved_table_userID] FOREIGN KEY ([userID]) REFERENCES [dbo].[administrator] ([userID])
);
GO

CREATE TABLE [dbo].[history](
    [userID] [int],
    [itemCode] [int] NOT NULL IDENTITY(1,1) PRIMARY KEY,
    [searchedDate] [datetime] NOT NULL,
    [itemName] [nvarchar] (255) NOT NULL,
    CONSTRAINT [FK_tbladministrator_tblhistory_userID] FOREIGN KEY ([userID]) REFERENCES [dbo].[administrator] ([userID])
);
GO