-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 05 Des 2020 pada 18.42
-- Versi server: 10.4.14-MariaDB
-- Versi PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tomcat_esport`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'mchevro', 'cubegaming');

-- --------------------------------------------------------

--
-- Struktur dari tabel `daftar_ml`
--

CREATE TABLE `daftar_ml` (
  `id` int(11) NOT NULL,
  `Team` varchar(100) NOT NULL,
  `NamaKapten` varchar(100) NOT NULL,
  `IGN_Kapten` varchar(100) NOT NULL,
  `ID_Kapten` bigint(4) NOT NULL,
  `NamaPlayer2` varchar(100) NOT NULL,
  `IGN_Player2` varchar(100) NOT NULL,
  `ID_Player2` bigint(4) NOT NULL,
  `NamaPlayer3` varchar(100) NOT NULL,
  `IGN_Player3` varchar(100) NOT NULL,
  `ID_Player3` bigint(4) NOT NULL,
  `NamaPlayer4` varchar(100) NOT NULL,
  `IGN_Player4` varchar(100) NOT NULL,
  `ID_Player4` bigint(4) NOT NULL,
  `NamaPlayer5` varchar(100) NOT NULL,
  `IGN_Player5` varchar(100) NOT NULL,
  `ID_Player5` bigint(4) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Whatsapp` varchar(20) NOT NULL,
  `BuktiPembayaran` varchar(255) NOT NULL,
  `Waktu` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `daftar_ml`
--

INSERT INTO `daftar_ml` (`id`, `Team`, `NamaKapten`, `IGN_Kapten`, `ID_Kapten`, `NamaPlayer2`, `IGN_Player2`, `ID_Player2`, `NamaPlayer3`, `IGN_Player3`, `ID_Player3`, `NamaPlayer4`, `IGN_Player4`, `ID_Player4`, `NamaPlayer5`, `IGN_Player5`, `ID_Player5`, `Email`, `Whatsapp`, `BuktiPembayaran`, `Waktu`) VALUES
(1, 'Evos Esport', 'Ikhsan Lemon', 'Lemon', 375736881, 'Yurino', 'Donkeey', 375736882, 'Papi', 'Marsha', 375736883, 'Jonathan', 'gusion', 375736884, 'Kevin', 'vynn', 375736885, 'oura@gmail.com', '081381662912', 'Evos Esport-142563.jpg', '2020-12-04 07:10:31');

-- --------------------------------------------------------

--
-- Struktur dari tabel `daftar_pubg`
--

CREATE TABLE `daftar_pubg` (
  `id` int(11) NOT NULL,
  `Team` varchar(100) NOT NULL,
  `NamaKapten` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `turnament`
--

CREATE TABLE `turnament` (
  `id` int(11) NOT NULL,
  `Thumbnail` varchar(255) NOT NULL,
  `Judul` varchar(255) NOT NULL,
  `Genre` text NOT NULL,
  `Biaya` varchar(10) NOT NULL,
  `Slot` int(1) NOT NULL,
  `Hadiah` varchar(10) NOT NULL,
  `Waktu` date NOT NULL,
  `Status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `turnament`
--

INSERT INTO `turnament` (`id`, `Thumbnail`, `Judul`, `Genre`, `Biaya`, `Slot`, `Hadiah`, `Waktu`, `Status`) VALUES
(1, 'MobileLegend.jpg', 'Mobile Legend | Telesandi Only', 'MLBB', '50.000', 35, '600.000', '2020-12-03', 1),
(2, 'Pubg.jpg', 'Player Uknown| Telesandi Only', 'PUBG', '150.000', 20, '800.000', '2020-12-31', 0),
(3, 'MobileLegend.jpg', 'Mobile Legend | Telesandi Only', 'MLBB', '50.000', 35, '600.000', '2021-01-20', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `turnament_jadwal`
--

CREATE TABLE `turnament_jadwal` (
  `id` int(11) NOT NULL,
  `Team` varchar(100) NOT NULL,
  `Jam` time NOT NULL,
  `Tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `turnament_jadwal`
--

INSERT INTO `turnament_jadwal` (`id`, `Team`, `Jam`, `Tanggal`) VALUES
(1, 'Bigetron VS Evos Esport', '11:32:48', '2020-12-05');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `daftar_ml`
--
ALTER TABLE `daftar_ml`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `daftar_pubg`
--
ALTER TABLE `daftar_pubg`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `turnament`
--
ALTER TABLE `turnament`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `turnament_jadwal`
--
ALTER TABLE `turnament_jadwal`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `daftar_ml`
--
ALTER TABLE `daftar_ml`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `daftar_pubg`
--
ALTER TABLE `daftar_pubg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `turnament`
--
ALTER TABLE `turnament`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `turnament_jadwal`
--
ALTER TABLE `turnament_jadwal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
