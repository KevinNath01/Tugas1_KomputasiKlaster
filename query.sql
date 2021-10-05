USE `kluster`

CREATE VIEW query_nilai AS
SELECT 
    `jawaban`.`id_siswa`,
    `soal`.`id_mapel`,
    SUM(`jawaban`.`pilihan_jawaban`=`soal`.`kunci_jawaban`)*2.5 AS nilai 
FROM `soal` 
    INNER JOIN `jawaban` ON `soal`.`id_soal` = `jawaban`.`id_soal` 
GROUP BY `jawaban`.`id_siswa`, `soal`.`id_mapel`;

-- SELECT 
-- 	`query_nilai`.`id_siswa`,
-- 	MAX(CASE WHEN `query_nilai`.`id_mapel`=1 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_1,
-- 	MAX(CASE WHEN `query_nilai`.`id_mapel`=2 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_2,
-- 	MAX(CASE WHEN `query_nilai`.`id_mapel`=3 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_3,
-- 	MAX(CASE WHEN `query_nilai`.`id_mapel`=4 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_4,
-- 	MAX(CASE WHEN `query_nilai`.`id_mapel`=5 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_5,
-- 	MAX(CASE WHEN `query_nilai`.`id_mapel`=6 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_6,
-- 	MAX(CASE WHEN `query_nilai`.`id_mapel`=7 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_7
-- FROM `query_nilai`
-- GROUP BY `query_nilai`.`id_siswa`;
