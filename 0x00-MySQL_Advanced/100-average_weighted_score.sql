--  creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score FLOAT DEFAULT 0;
	DECLARE total_weight FLOAT DEFAULT 0;
	SELECT SUM(c.score * p.weight), SUM(p.weight)
	INTO total_score, total_weight
	FROM corrections c
	INNER JOIN projects p ON c.project_id = p.id
	WHERE c.user_id = user_id;

	UPDATE users
	SET average_score = total_score / total_weight
	WHERE id = user_id;
END //
DELIMITER ;
