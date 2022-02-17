create table grupos(
codgrupo varchar(3) primary key,
nombre_grupo varchar(50),
descripcion_grupo text,
estado bool);

insert into grupos(codgrupo,nombre_grupo, descripcion_grupo, estado)
values('G5','SINGRUPO','Este es un grupo de prueba', True);

insert into grupos(codgrupo,nombre_grupo,descripcion_grupo,estado)
values('G1','ECO INDUSTRIA','Grupo 1',True);

insert into grupos(codgrupo,nombre_grupo,descripcion_grupo,estado)
values('G2','ATRAYENDO TALENTO','Grupo 2',True);

insert into grupos(codgrupo,nombre_grupo,descripcion_grupo,estado)
values('G3','TECHINNOVATION','Grupo 3',True);

insert into grupos(codgrupo,nombre_grupo,descripcion_grupo,estado)
values('G4','YOURLIFEWITHUS','Grupo 4',True);


select * from grupos;