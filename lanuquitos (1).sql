-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 29-06-2023 a las 20:46:48
-- Versión del servidor: 8.0.17
-- Versión de PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `lanuquitos`
--

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `nombre`) VALUES
(1, 'Llaveros'),
(2, 'Animales');

--
-- Volcado de datos para la tabla `imagen`
--

INSERT INTO `imagen` (`id`, `ruta`) VALUES
(1, 'Mr_MsPacman.jpg'),
(2, 'mono.jpg');

--
-- Volcado de datos para la tabla `imagen_lanuquito`
--

INSERT INTO `imagen_lanuquito` (`id`, `id_lanuquito`, `id_imagen`) VALUES
(1, 1, 1),
(2, 2, 2);

--
-- Volcado de datos para la tabla `lanuquito`
--

INSERT INTO `lanuquito` (`id`, `nombre`, `precio`, `id_categoria`) VALUES
(1, 'Llavero Pacman', 1250, 1),
(2, 'Mono Lucio', 3400, 2);

--
-- Volcado de datos para la tabla `material`
--

INSERT INTO `material` (`id`, `material`, `precio`, `proveedor`) VALUES
(1, 'Lana acrilica Amarilo COD  24', 200, 'Tejidos Telar'),
(2, 'Lana acrilica Negro COD 99', 200, 'Tejidos Telar'),
(3, 'Ojo Plastico N1', 50, 'ML'),
(4, 'Cadena llavero', 75, 'ML');

--
-- Volcado de datos para la tabla `material_lanuquito`
--

INSERT INTO `material_lanuquito` (`id`, `id_lanuquito`, `id_materiales`, `cantidad`, `precio`) VALUES
(1, 1, 1, 10, NULL),
(2, 1, 4, 1, NULL),
(3, 2, 2, 150, NULL),
(4, 2, 3, 2, NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
