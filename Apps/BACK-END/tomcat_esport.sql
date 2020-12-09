-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 09 Des 2020 pada 12.19
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
-- Struktur dari tabel `bukti_pembayaran`
--

CREATE TABLE `bukti_pembayaran` (
  `id` int(11) NOT NULL,
  `Team` varchar(100) NOT NULL,
  `Foto` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `bukti_pembayaran`
--

INSERT INTO `bukti_pembayaran` (`id`, `Team`, `Foto`) VALUES
(1, 'Rex Regum Qeon', 'Rex Regum Qeon-56-09-December.jpg'),
(2, 'Evos Esport', 'Evos Esport-45-09-December.jpg'),
(3, 'Alter Ego', 'Alter Ego-57-09-December.jpg');

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
  `Waktu` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `daftar_ml`
--

INSERT INTO `daftar_ml` (`id`, `Team`, `NamaKapten`, `IGN_Kapten`, `ID_Kapten`, `NamaPlayer2`, `IGN_Player2`, `ID_Player2`, `NamaPlayer3`, `IGN_Player3`, `ID_Player3`, `NamaPlayer4`, `IGN_Player4`, `ID_Player4`, `NamaPlayer5`, `IGN_Player5`, `ID_Player5`, `Email`, `Whatsapp`, `Waktu`) VALUES
(1, 'Rex Regum Qeon', 'asd', 'asd', 213, 'asd', 'asd', 213, 'asd', 'asd', 213, 'asd', 'asd', 213, 'asd', 'asd', 213, 'asdasd@gmail.com', '123213', '2020-12-09 10:41:35'),
(2, 'Evos Esport', 'Eko Julyano', 'ouraa', 1, 'Yurino', 'donkey', 2, 'Ikhsan', 'lemon', 3, 'Firdaus', 'luminare', 4, 'Jonathan Liandi', 'joo', 5, 'evos@gmail.com', '081381662912', '2020-12-09 10:50:28'),
(3, 'Alter Ego', 'Muhammad Julian ', 'Udil', 1, 'Ahmad Abdurrahman ', 'Ahmad ', 2, 'Eldin Rahadian Putra ', 'Celiboy', 3, 'Julian Murphy ', 'LeoMurphy ', 4, 'Ilyas Rahmanda ', 'Caesius ', 5, 'delwyn@alterego.com', '0821231233', '2020-12-09 11:08:46'),
(4, 'Onic Esport', 'Muhammad Julian ', 'Udil', 1, 'Ahmad Abdurrahman ', 'Ahmad ', 2, 'Eldin Rahadian Putra ', 'Celiboy', 3, 'Julian Murphy ', 'LeoMurphy ', 4, 'Ilyas Rahmanda ', 'Caesius ', 5, 'delwyn@alterego.com', '0821231233', '2020-12-09 11:08:46');

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
  `Genre` varchar(6) NOT NULL,
  `Biaya` varchar(10) NOT NULL,
  `Slot` varchar(10) NOT NULL,
  `Hadiah` varchar(10) NOT NULL,
  `Waktu` date NOT NULL,
  `Status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `turnament`
--

INSERT INTO `turnament` (`id`, `Thumbnail`, `Judul`, `Genre`, `Biaya`, `Slot`, `Hadiah`, `Waktu`, `Status`) VALUES
(5, 'FF-09-December-2020.jpg', 'Free Fire | Umum', 'FF', '90.000', '0/50', '1.500.000', '2020-12-01', 0),
(6, 'MLBB-09-December-2020.jpg', 'Mobile Legend | Umum', 'MLBB', '90.000', '0/32', '800.000', '2020-12-18', 1);

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
-- Indeks untuk tabel `bukti_pembayaran`
--
ALTER TABLE `bukti_pembayaran`
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
-- AUTO_INCREMENT untuk tabel `bukti_pembayaran`
--
ALTER TABLE `bukti_pembayaran`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `turnament_jadwal`
--
ALTER TABLE `turnament_jadwal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
