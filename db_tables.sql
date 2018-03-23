#create city table
CREATE TABLE `city` (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`geoname_id` bigint(20) NOT NULL COMMENT 'geoname id',
`name` varchar(200) DEFAULT '' COMMENT 'city name',
`ascii_name` varchar(200) DEFAULT '' COMMENT 'city ascii name',
`display_name` varchar(200) DEFAULT '' COMMENT 'city display name',
`lat` int(11) DEFAULT NULL COMMENT 'city latitude',
`lng` int(11) DEFAULT NULL COMMENT 'city longitude',
`country_code` varchar(16) DEFAULT '' COMMENT 'country code, like CN, US',
`admin1_code` varchar(20) DEFAULT '' COMMENT 'admin1 code',
`time_zone_desc` varchar(40) DEFAULT '' COMMENT 'time zone description, like Asia/Shanghai', 
`time_zone_offset` float DEFAULT NULL COMMENT 'time zone offset by hours', 
`country_name` varchar(512) DEFAULT '' COMMENT 'city country name', 
`state_name` varchar(512) DEFAULT '' COMMENT 'city state name',
`feature_code` varchar(10) DEFAULT '' COMMENT 'city feature code',
`population` int(11) DEFAULT '0' COMMENT 'city population',
`search_priority` int(11) DEFAULT '0' COMMENT 'search priority',
`valid` tinyint(2) DEFAULT NULL COMMENT 'valid=0 deleted',
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='city table';


#create city alternate names table
CREATE TABLE `city_alternatenames` (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`geoname_id` bigint(20) NOT NULL COMMENT 'geoname id',
`city_ascii_name` varchar(200) NOT NULL COMMENT 'city ascii name', 
`alternate_name` varchar(200) NOT NULL COMMENT 'city alternate name',
`language` varchar(10) DEFAULT '' COMMENT 'city alternate name language code, like CN',
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='city alternate names table';
