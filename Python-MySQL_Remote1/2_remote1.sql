SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- --------------------------------------------------------

--
-- 資料表結構 `member`
--

CREATE TABLE `member` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `birthday` date NOT NULL DEFAULT '0000-00-00',
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `member`
--

INSERT INTO `member` (`id`, `name`, `birthday`, `address`) VALUES
(1, '測試', '2018-11-01', '測試測試'),
(2, '測試2', '2018-11-22', '測試2測試2'),
(3, 'xxx', '2011-11-10', 'xxxxxx'),
(4, 'bbb', '2018-10-10', 'bbbbbb'),
(5, 'ccc', '2018-11-01', 'ccccc'),
(10, '實驗1', '2018-11-05', '實驗1'),
(11, '哈哈', '2011-11-11', '哈哈哈'),
(12, '測試你', '2010-10-21', '測試'),
(20, '您好', '2011-11-11', '您好歡迎光臨'),
(21, '測試測試', '1950-05-05', '測試測試AAAA'),
(22, '哈囉', '2010-10-10', '哈囉哈囉');

-- --------------------------------------------------------

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id`);


--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `member`
--
ALTER TABLE `member`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
