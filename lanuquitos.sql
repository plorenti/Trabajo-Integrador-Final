-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 29-06-2023 a las 20:01:01
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `nombre`) VALUES
(1, 'Llaveros'),
(2, 'Animales');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `imagen`
--

CREATE TABLE `imagen` (
  `id` int(11) NOT NULL,
  `ruta` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `imagen`
--

INSERT INTO `imagen` (`id`, `ruta`) VALUES
(1, 'Mr_MsPacman.jpg'),
(2, 'mono.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `imagen_lanuquito`
--

CREATE TABLE `imagen_lanuquito` (
  `id` int(11) NOT NULL,
  `id_lanuquito` int(11) DEFAULT NULL,
  `id_imagen` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `imagen_lanuquito`
--

INSERT INTO `imagen_lanuquito` (`id`, `id_lanuquito`, `id_imagen`) VALUES
(1, 1, 1),
(2, 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lanuquito`
--

CREATE TABLE `lanuquito` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `lanuquito`
--

INSERT INTO `lanuquito` (`id`, `nombre`, `precio`, `id_categoria`) VALUES
(1, 'Llavero Pacman', 1250, 1),
(2, 'Mono Lucio', 3400, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materiales`
--

CREATE TABLE `material` (
  `id` int(11) NOT NULL,
  `material` varchar(200) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `proveedor` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `materiales`
--

INSERT INTO `material` (`id`, `material`, `precio`, `proveedor`) VALUES
(1, 'Lana acrilica Amarilo COD  24', 200, 'Tejidos Telar'),
(2, 'Lana acrilica Negro COD 99', 200, 'Tejidos Telar'),
(3, 'Ojo Plastico N1', 50, 'ML'),
(4, 'Cadena llavero', 75, 'ML');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `material_lanuquito`
--

CREATE TABLE `material_lanuquito` (
  `id` int(11) NOT NULL,
  `id_lanuquito` int(11) DEFAULT NULL,
  `id_materiales` int(11) DEFAULT NULL,
  `cantidad` double DEFAULT NULL,
  `precio` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `material_lanuquito`
--

INSERT INTO `material_lanuquito` (`id`, `id_lanuquito`, `id_materiales`, `cantidad`, `precio`) VALUES
(1, 1, 1, 10, NULL),
(2, 1, 4, 1, NULL),
(3, 2, 2, 150, NULL),
(4, 2, 3, 2, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `imagen`
--
ALTER TABLE `imagen`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `imagen_lanuquito`
--
ALTER TABLE `imagen_lanuquito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_lanuquito` (`id_lanuquito`),
  ADD KEY `id_imagen` (`id_imagen`);

--
-- Indices de la tabla `lanuquito`
--
ALTER TABLE `lanuquito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `materiales`
--
ALTER TABLE `material`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `material_lanuquito`
--
ALTER TABLE `material_lanuquito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_lanuquito` (`id_lanuquito`),
  ADD KEY `id_materiales` (`id_materiales`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `imagen`
--
ALTER TABLE `imagen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `imagen_lanuquito`
--
ALTER TABLE `imagen_lanuquito`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `lanuquito`
--
ALTER TABLE `lanuquito`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `materiales`
--
ALTER TABLE `material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `material_lanuquito`
--
ALTER TABLE `material_lanuquito`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `imagen_lanuquito`
--
ALTER TABLE `imagen_lanuquito`
  ADD CONSTRAINT `imagen_lanuquito_ibfk_1` FOREIGN KEY (`id_lanuquito`) REFERENCES `lanuquito` (`id`),
  ADD CONSTRAINT `imagen_lanuquito_ibfk_2` FOREIGN KEY (`id_imagen`) REFERENCES `imagen` (`id`);

--
-- Filtros para la tabla `lanuquito`
--
ALTER TABLE `lanuquito`
  ADD CONSTRAINT `lanuquito_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id`);

--
-- Filtros para la tabla `material_lanuquito`
--
ALTER TABLE `material_lanuquito`
  ADD CONSTRAINT `material_lanuquito_ibfk_1` FOREIGN KEY (`id_lanuquito`) REFERENCES `lanuquito` (`id`),
  ADD CONSTRAINT `material_lanuquito_ibfk_2` FOREIGN KEY (`id_materiales`) REFERENCES `material` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
