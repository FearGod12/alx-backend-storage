-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE user_id INT;
	DECLARE counter INT DEFAULT 1;
	DECLARE total_users INT;
	DECLARE total_score FLOAT DEFAULT 0;
        DECLARE total_weight FLOAT DEFAULT 0;

	SELECT COUNT(*) INTO total_users FROM users;

	CREATE TEMPORARY TABLE temp_user_ids (id INT);

	INSERT INTO temp_user_ids (id) SELECT id FROM users;

	WHILE counter <= total_users DO

		SELECT id INTO user_id FROM temp_user_ids LIMIT counter, 1;
		
		SELECT SUM(c.score * p.weight), SUM(p.weight)
		INTO total_score, total_weight
		FROM corrections c
		INNER JOIN projects p ON c.project_id = p.id
		WHERE c.user_id = user_id;

		UPDATE users
		SET average_score = total_score / total_weight
		WHERE id = user_id;

		SET counter = counter + 1;
	END WHILE;
	DROP TABLE temp_user_ids;
END //
DELIMITER ;
