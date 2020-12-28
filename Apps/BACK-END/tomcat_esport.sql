-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 27 Des 2020 pada 13.49
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
  `Foto` varchar(255) NOT NULL,
  `Genre` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `bukti_pembayaran`
--

INSERT INTO `bukti_pembayaran` (`id`, `Team`, `Foto`, `Genre`) VALUES
(1, 'Alter Ego', 'Alter Ego-02-09-December.jpg', 'MLBB'),
(2, 'Evos Legend', 'Evos Legend-13-09-December.jpg', 'MLBB'),
(3, 'Onic Esport', 'Onic Esport-52-20-December.jpg', 'MLBB'),
(4, 'Saints Indo', 'Saints Indo-49-20-December.jpg', 'MLBB'),
(5, 'Elite 8', 'Elite 8-564333-20-December.jpg', 'MLBB'),
(6, 'Team Tels', 'Team Tels-503639-20-December.jpg', 'MLBB');

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
(1, 'Alter Ego', 'Ahmad Abdurrahman ', 'Ahmad ', 1, 'Julian Murphy ', 'LeoMurphy ', 2, 'Eldin Rahadian Putra ', 'Celiboy', 3, 'William W ', 'YAM? ', 4, 'Rafly Alvareza Sudrajat ', 'PAI ', 5, 'alterego@gmail.com', '081381662912', '2020-12-09 15:53:48'),
(2, 'Evos Legend', 'Gustian ', 'R E K T ', 1, 'Fahmi Adam Alamsyah ', 'Rexxy ', 2, 'Muhammad Ridwan ', 'Wannn ', 3, 'Raihan Delvino Ardy ', 'Bajan ', 4, 'Sebastian Arthur ', 'Pendragon ', 5, 'evos@evos.com', '08463678923', '2020-12-09 15:24:48'),
(3, 'Onic Esport', 'Gustian', 'R E K T ', 1, 'Fahmi Adam Alamsyah ', 'Rexxy ', 2, 'Muhammad Ridwan ', 'Wannn ', 3, 'Raihan Delvino Ardy ', 'Bajan ', 4, 'Sebastian Arthur ', 'Pendragon ', 5, 'evos@evos.com', '08463678923', '2020-12-20 16:43:00'),
(5, 'Saints Indo', 'asd', 'asd', 1, 'asd', 'asd', 2, 'asd', 'asd', 3, 'asd', 'asd', 4, 'asd', 'asd', 5, 'asdasd@gmail.com', '123123', '2020-12-20 16:43:40'),
(6, 'Elite 8', 'asdag', 'klm', 1, 'aga', 'km ni', 2, 'ag', 'nnoij[', 3, 'asde', 'mopmpo', 4, 'hgaw', 'unbuonf', 5, 'asd@google.com', '081381662912', '2020-12-20 16:45:54'),
(7, 'Team Tels', 'Sasd', 'Hsjsj', 1, 'AssBsjs', 'Bdhs', 2, 'Nsnns', 'Hsjd', 3, 'Hshsh', 'Hsjs', 4, 'Jsjs', 'Bsbs', 5, 'tels@google.com', '08124567845', '2020-12-20 16:50:54');

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
  `Tanggal` date NOT NULL,
  `Genre` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `turnament_jadwal`
--

INSERT INTO `turnament_jadwal` (`id`, `Team`, `Jam`, `Tanggal`, `Genre`) VALUES
(1, 'BTR VS Evos Esport', '11:30:00', '2020-12-05', 'MLBB'),
(2, 'BTR VS PUBG', '11:30:00', '2020-12-05', 'PUBG'),
(3, 'Onic VS PB', '11:30:00', '2020-12-05', 'PB'),
(4, 'Elit 8 VS PUBG', '11:30:00', '2020-12-05', 'PUBG'),
(5, 'BTR VS Evos Esport', '11:30:00', '2020-12-05', 'MLBB'),
(6, 'BTR VS PUBG', '11:30:00', '2020-12-05', 'PUBG'),
(7, 'Onic VS PB', '11:30:00', '2020-12-05', 'PB'),
(8, 'Elit 8 VS PUBG', '11:30:00', '2020-12-05', 'PUBG'),
(9, 'BTR VS Evos Esport', '11:30:00', '2020-12-05', 'MLBB'),
(10, 'BTR VS PUBG', '11:30:00', '2020-12-05', 'PUBG'),
(11, 'Onic VS PB', '11:30:00', '2020-12-05', 'PB'),
(12, 'Elit 8 VS PUBG', '11:30:00', '2020-12-05', 'PUBG'),
(13, 'BTR VS Evos Esport', '11:30:00', '2020-12-05', 'MLBB'),
(14, 'BTR VS PUBG', '11:30:00', '2020-12-05', 'PUBG'),
(15, 'Onic VS PB', '11:30:00', '2020-12-05', 'PB'),
(16, 'Elit 8 VS PUBG', '11:30:00', '2020-12-05', 'PUBG');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `daftar_ml`
--
ALTER TABLE `daftar_ml`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
