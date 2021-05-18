-- CREATE SCHEMA `chatbot` DEFAULT CHARACTER SET utf8mb4 ;
-- USE chatbot;

--
-- 資料表結構 `bot_options`
--

CREATE TABLE `bot_options` (
  `option_id` bigint(20) UNSIGNED NOT NULL,
  `option_name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `option_value` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `autoload` varchar(20) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'yes'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 資料表索引 `bot_options`
--
ALTER TABLE `bot_options`
  ADD PRIMARY KEY (`option_id`),
  ADD UNIQUE KEY `option_name` (`option_name`),
  ADD KEY `autoload` (`autoload`);

-- --------------------------------------------------------

--
-- 資料表結構 `bot_chatmeta`
--

CREATE TABLE `bot_chatmeta` (
  `meta_id` bigint(20) UNSIGNED NOT NULL,
  `chat_id` bigint(20) UNSIGNED NOT NULL DEFAULT '0',
  `meta_key` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `meta_value` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 資料表索引 `bot_chatmeta`
--
ALTER TABLE `bot_chatmeta`
  ADD PRIMARY KEY (`meta_id`),
  ADD KEY `chat_id` (`chat_id`),
  ADD KEY `meta_key` (`meta_key`(255));

-- --------------------------------------------------------

--
-- 資料表結構 `bot_chats`
--

CREATE TABLE `bot_chats` (
  `ID` bigint(20) UNSIGNED NOT NULL,
  `chat_user` bigint(20) UNSIGNED NOT NULL DEFAULT '0',
  `chat_datetime` datetime NOT NULL DEFAULT '1900-01-01 00:00:00',
  `chat_ask` text COLLATE utf8mb4_general_ci NOT NULL,  
  `bot_response` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `bot_response_type` varchar(100) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'message',
  `chat_parent` bigint(20) UNSIGNED NOT NULL DEFAULT '0',
  `chat_intent` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `chat_entity` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `chat_context` text COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 資料表索引 `bot_chats`
--
ALTER TABLE `bot_chats`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `bot_response_type` (`bot_response_type`(100)),
  ADD KEY `chat_intent` (`chat_intent`(255)),
  ADD KEY `chat_entity` (`chat_entity`(255)),
  ADD KEY `chat_parent` (`chat_parent`),
  ADD KEY `chat_user` (`chat_user`);

-- --------------------------------------------------------

--
-- 資料表結構 `bot_usermeta`
--

CREATE TABLE `bot_usermeta` (
  `umeta_id` bigint(20) UNSIGNED NOT NULL,
  `user_id` bigint(20) UNSIGNED NOT NULL DEFAULT '0',
  `meta_key` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `meta_value` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 資料表索引 `bot_usermeta`
--
ALTER TABLE `bot_usermeta`
  ADD PRIMARY KEY (`umeta_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `meta_key` (`meta_key`(255));

-- --------------------------------------------------------

--
-- 資料表結構 `bot_users`
--

CREATE TABLE `bot_users` (
  `ID` bigint(20) UNSIGNED NOT NULL,
  `telegram_user_id` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `telegram_chat_id` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `user_nicename` varchar(50) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `user_email` varchar(100) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `user_phone` varchar(100) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `user_status` int(11) NOT NULL DEFAULT '0',
  `display_name` varchar(250) COLLATE utf8mb4_general_ci NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 資料表索引 `bot_users`
--
ALTER TABLE `bot_users`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `telegram_user_id` (`telegram_user_id`),
  ADD KEY `telegram_chat_id` (`telegram_chat_id`),
  ADD KEY `user_nicename` (`user_nicename`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `bot_options`
--
ALTER TABLE `bot_options`
  MODIFY `option_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `bot_chatmeta`
--
ALTER TABLE `bot_chatmeta`
  MODIFY `meta_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `bot_chats`
--
ALTER TABLE `bot_chats`
  MODIFY `ID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `bot_usermeta`
--
ALTER TABLE `bot_usermeta`
  MODIFY `umeta_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `bot_users`
--
ALTER TABLE `bot_users`
  MODIFY `ID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;