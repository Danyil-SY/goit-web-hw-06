SELECT s.student_id, s.student_name, g.group_name
FROM students s 
JOIN groups g ON s.group_id = g.group_id
WHERE s.group_id = 1;