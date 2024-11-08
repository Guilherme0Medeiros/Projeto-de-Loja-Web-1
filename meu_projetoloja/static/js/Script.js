// Seleciona os elementos necessários
const gameSelect = document.getElementById('disabledSelect1');
const priceDisplay = document.getElementById('gamePrice');
const paymentSelect = document.getElementById('disabledSelect3');
const finalizePurchaseBtn = document.getElementById('finalizePurchaseBtn');

// Event listener para atualizar o preço baseado na seleção
gameSelect.addEventListener('change', function() {
  const selectedPrice = parseInt(gameSelect.value) || 90; // Pega o valor do preço ou padrão 90
  priceDisplay.textContent = `R$ ${selectedPrice},00`;
});

// Função de validação e alerta de compra finalizada
finalizePurchaseBtn.addEventListener('click', function() {
  const radioOptions = document.querySelector('input[name="inlineRadioOptions"]:checked');
  const gameSelected = gameSelect.value;
  const paymentSelected = paymentSelect.value;

  // Verifica se todas as opções foram selecionadas
  if (!radioOptions) {
    alert('Selecione se é um presente.');
  } else if (gameSelected === "") {
    alert('Selecione uma versão do jogo.');
  } else if (paymentSelected === "") {
    alert('Selecione uma forma de pagamento.');
  } else {
    // Se todas as opções estiverem preenchidas, exibe o alerta de compra
    alert("Compra finalizada com sucesso!");
  }
});
