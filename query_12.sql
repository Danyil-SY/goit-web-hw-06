SELECT s.student_id, s.student_name, g.grade
FROM grades g
JOIN students s ON g.student_id = s.student_id
WHERE g.subject_id = 1 AND s.group_id = 1 AND g.date_received = (
    SELECT MAX(date_received) FROM grades WHERE subject_id = 1
);