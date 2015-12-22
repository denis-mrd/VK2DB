USE [VK]
GO

/****** Object:  Table [dbo].[friends]    Script Date: 20.11.2015 14:49:23 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[friends](
	[id] [int] NOT NULL,
	[domain] [nvarchar](max) NULL,
	[last_name] [nvarchar](max) NULL,
	[first_name] [nvarchar](max) NULL,
	[sex] [nvarchar](max) NULL,
	[bdate] [nvarchar](max) NULL,
	[city_title] [nvarchar](max) NULL,
	[country_title] [nvarchar](max) NULL,
	[mobile_phone] [nvarchar](max) NULL,
	[home_phone] [nvarchar](max) NULL,
	[facebook] [nvarchar](max) NULL,
	[instagram] [nvarchar](max) NULL,
	[twitter] [nvarchar](max) NULL,
	[skype] [nvarchar](max) NULL,
	[site] [nvarchar](max) NULL,
	[relation] [nvarchar](max) NULL,
	[relation_partner_id] [nvarchar](max) NULL,
	[personal_political] [nvarchar](max) NULL,
	[personal_life_main] [nvarchar](max) NULL,
	[personal_people_main] [nvarchar](max) NULL,
	[personal_smoking] [nvarchar](max) NULL,
	[personal_alcohol] [nvarchar](max) NULL,
	[photo_max_orig] [nvarchar](max) NULL,
	
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO


