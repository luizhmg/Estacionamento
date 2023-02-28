'''Criação da tabela Funcionarios'''
CREATE TABLE `funcionarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `cpf` varchar(20) unique,
  `senha` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

'''Criação da tabela pessoas'''
CREATE TABLE `pessoas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `cpf` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

'''Criação da tabela Vagas'''
CREATE TABLE `vagas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seçao` varchar(10) DEFAULT NULL,
  `numero` int(11) DEFAULT NULL,
  `andar` varchar(3) DEFAULT NULL,
  `tipo` varchar(10) DEFAULT NULL,
  `bloco` varchar(2) DEFAULT NULL,
  `idveiculo` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idveiculo_idx` (`idveiculo`),
  CONSTRAINT `idveiculo` FOREIGN KEY (`idveiculo`) REFERENCES `veiculos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=latin1;

'''Criação da tabela Veiculos'''
CREATE TABLE `veiculos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `marca` varchar(45) DEFAULT NULL,
  `modelo` varchar(20) DEFAULT NULL,
  `cor` varchar(15) DEFAULT NULL,
  `placa` varchar(18) DEFAULT NULL,
  `idproprietario` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idproprietario_idx` (`idproprietario`),
  CONSTRAINT `idproprietario` FOREIGN KEY (`idproprietario`) REFERENCES `pessoas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;


