ALTER TABLE `chatbot`.`bot_chats` 
ADD COLUMN `chat_action` VARCHAR(255) NOT NULL DEFAULT '' AFTER `chat_intent`;
