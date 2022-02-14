use bdcargamos;
show tables;
select * from alumnos;
select * from grupos;

/*Alumnos del grupo 1*/
select * from alumnos where codgrupo = 'G1';
select * from alumnos where codgrupo = 'G2';
select * from alumnos where codgrupo = 'G3';
select * from alumnos where codgrupo = 'G4';
select * from alumnos where codgrupo = 'G5';

insert into productos(id,nombre_producto, precio, state)
values(1,"chocolate con fresa", 20, True);
insert into productos(id,nombre_producto, precio, state)
values(2,"chocolate con locuma", 25, True);
insert into productos(id,nombre_producto, precio, state)
values(3,"chocolate con limon", 30, True);
insert into productos(id,nombre_producto, precio, state)
values(4,"chocolate con coco", 40, True);