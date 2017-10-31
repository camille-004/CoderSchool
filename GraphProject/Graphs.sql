CREATE SCHEMA graph_db;

CREATE TABLE `nodes` (
	`id` INT(10) PRIMARY KEY,
    `val` VARCHAR(30)
);

CREATE TABLE `neighbors` (
	`node_id` INT(10),
    `neighbor_id` INT(10)
);
CREATE INDEX idx_node ON neighbors (node_id);


INSERT INTO nodes (id, val) VALUES (1, "hello");
INSERT INTO nodes (id, val) VALUES (2, "helloo");
INSERT INTO nodes (id, val) VALUES (3, "hellooo");

INSERT INTO neighbors (node_id, neighbor_id) VALUES (1, 2);
INSERT INTO neighbors (node_id, neighbor_id) VALUES (1, 3);

SELECT * FROM nodes WHERE id = 1;
SELECT * FROM neighbors WHERE node_id = 1;

SELECT * FROM nodes;
SELECT * FROM neighbors;