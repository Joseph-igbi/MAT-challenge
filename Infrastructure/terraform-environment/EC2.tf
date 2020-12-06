
resource "aws_instance" "bastion_host" {
  ami                         = var.ami
  instance_type               = "t2.micro"
  key_name                    = var.key_name
  subnet_id                   = aws_subnet.public_subnet.id
  vpc_security_group_ids      = [aws_security_group.sgbh.id]
  associate_public_ip_address = true

  tags = {
    Name = "bastionhost"
  }
}

resource "aws_instance" "private_host" {
  ami                    = var.ami
  instance_type          = "t2.micro"
  key_name               = var.key_name
  subnet_id              = aws_subnet.private_subnet.id
  vpc_security_group_ids = [aws_security_group.sgph.id]
  user_data              = "$(file('user_data.sh')"
  tags = {
    Name = "private_host"
  }
}





