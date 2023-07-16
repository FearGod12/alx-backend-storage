-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id VARCHAR(255))
BEGIN
	DECLARE averag_score FLOAT;
	SELECT AVG(score) INTO averag_score
	FROM corrections
	WHERE user_id = user_id;

	UPDATE users SET average_score = averag_score
	WHERE id = user_id;
END //
DELIMITER ;
