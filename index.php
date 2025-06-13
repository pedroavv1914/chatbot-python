<?php

$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'bot_curso';
$conn = mysqli_connect($servidor,$usuario,$senha,$banco);

$numero_telefone = $_GET['telefone'];
$msg = $_GET['msg'];
$usuario = $_GET['usuario'];


$sql = "SELECT * FROM usuario WHERE telefone = '$numero_telefone'";
$query = mysqli_query($conn,$sql);
$total = mysqli_num_rows($query);

$status = 1;
$resposta = '';

while($rows_usuarios = mysqli_fetch_array($query)){
    $status = $rows_usuarios['status'];
}

?>

<?php

$menu2 = "Bem-vindo à Pizzarium! Que bom ter você aqui! Sou o Cheffino e estou aqui para ajudá-lo a fazer seu pedido de forma rápida e fácil. 
Para começar, digite CARDÁPIO para ver nossas opções de pizzas. 
Horário de atendimento: de Terça - Domingo, 16:00 as 00:00. Endereço: Rua Palestra Itália 51.
Estamos prontos para preparar sua pizza favorita!";

$menu3 = "CARDÁPIO DA Pizzarium
Descubra nossas delícias, feitas com amor e ingredientes fresquinhos!

...:PIZZAS CONVENCIONAIS:...
MUSSARELA = Molho de tomate, queijo mussarela e orégano. Tamanho: Média R$30 | Grande R$40

CALABRESA = Molho de tomate, calabresa fatiada, cebola e orégano. Tamanho: Média R$32 | Grande R$42

MARGUERITA= Molho de tomate, mussarela, tomate fresco e manjericão. Tamanho: Média R$33 | Grande R$43

FRANGO COM CATUPIRY = Frango desfiado, molho de tomate, catupiry e orégano. Tamanho: Média R$35 | Grande R$45

PORTUGUESA = Molho de tomate, mussarela, presunto, ovo, cebola, azeitonas e orégano. Tamanho: Média R$35 | Grande R$45

NAPOLITANA = Molho de tomate, mussarela, parmesão, tomate fresco e orégano.Tamanho: Média R$34 | Grande R$44

QUATRO QUEIJOS = Mussarela, gorgonzola, parmesão e catupiry. Tamanho: Média R$36 | Grande R$46

...:PIZZAS ESPECIAIS:...

PICANHA BBQ = Picanha desfiada, molho barbecue, mussarela e cebola caramelizada. Tamanho: Média R$45 | Grande R$55

ITÁLIA PREMIUM = Molho de tomate, mussarela de búfala, presunto de parma e rúcula. Tamanho: Média R$50 | Grande R$60

DOCE DELÍCIA = Base de chocolate ao leite, morangos frescos e granulado crocante. Tamanho: Média R$38 | Grande R$48";

$menu4 = "Você prefere pegar aqui, ou que seja entregue?";

$menu5 = "Qual método de pagamento você prefere? (PIX, Cartão Crédito/Débito, Dinheiro.)";

$menu6 = '';

?>

<?php

if($total == 0){

$sql = "INSERT INTO usuario (telefone,status) VALUES ('$numero_telefone', '1')";
$query = mysqli_query($conn,$sql);
if($query){

echo "Bem-vindo à Pizzarium! Que bom ter você aqui! Sou o Cheffino e estou aqui para ajudá-lo a fazer seu pedido de forma rápida e fácil. 
Para começar, digite CARDÁPIO para ver nossas opções de pizzas. 
Horário de atendimento: de Terça - Domingo, 16:00 as 00:00. Endereço: Rua Palestra Itália 51.
Estamos prontos para preparar sua pizza favorita!";    
}

}

if($total == 1){

    if($status == 1){

        $resposta = $menu2;

    }

    if($status == 2){

        $resposta = $menu3; 
    }

    if($status == 3){

        $resposta = $menu4;

    }

    if($status == 4){

        $resposta = $menu5; 

    }
  
}

if($status < 5){
    echo $resposta;

    $status2 = $status + 1 ;
    $sql = "UPDATE usuario SET status = '$status2' WHERE telefone = '$numero_telefone'";
    $query = mysqli_query($conn, $sql);

}

if($status >= 5){

    echo "Pedido confirmado! O prazo de entrega é de 20 - 40 minutos.
    Muito obrigado pela preferência!";
    
    $status2 = $status + 1 ;
    $sql = "UPDATE usuario SET status = '1' WHERE telefone = '$numero_telefone'";
    $query = mysqli_query($conn, $sql);
    
}

?>