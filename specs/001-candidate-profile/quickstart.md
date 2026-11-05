# Quickstart & Validation Guide: Candidate Profile & Base Resume Management

**Feature Branch**: `001-candidate-profile`  
**Date**: 2026-11-04  
**Status**: Concluído

## 1. Pré-Requisitos

- **Python**: 3.11+ com ambiente virtual configurado em `backend/.venv`
- **Node.js**: v20+ / npm 10+
- **PostgreSQL**: Instância operacional local ou contêiner com string de conexão em `.env`

---

## 2. Cenários de Validação Automatizados

### Backend (Pytest)

Executar os testes automatizados da suíte Python garantindo isolamento de repositório, validações de esquemas Pydantic e respostas da API:

```powershell
$env:PYTHONPATH="backend"
backend\.venv\Scripts\pytest.exe backend/tests -v
```

*Resultado Esperado:*
- `backend/tests/unit/test_profile_schemas.py`: Sucesso na validação de campos obrigatórios, datas e esquemas.
- `backend/tests/integration/test_profile_repository.py`: Sucesso na gravação, atualização atômica e exclusão em cascata.
- `backend/tests/api/test_profile_api.py`: Sucesso nos endpoints `GET`, `PUT` e `DELETE /api/v1/profile`.

---

### Frontend (Vitest & RTL)

Executar os testes de renderização, formulário e componentes atômicos:

```powershell
cd frontend
npm test -- --run
```

*Resultado Esperado:*
- Componentes `Button`, `Input`, `Badge`, `Card` validados com foco, estados de loading/disabled e estilos.
- `ProfileSection` testado com preenchimento, submissão e tratamento de estados.

---

### Compilação de Produção Frontend

Garantir ausência total de erros TypeScript e integridade do bundle Vite:

```powershell
cd frontend
npm run build
```

*Resultado Esperado:*
- `tsc -b` executado sem erros de tipos (`zero any`).
- `vite build` gerando os assets compilados em `frontend/dist/`.

---

## 3. Validação Manual End-to-End

1. Iniciar o servidor backend:
   ```powershell
   $env:PYTHONPATH="backend"
   backend\.venv\Scripts\python.exe -m uvicorn app.main:app --port 8000 --reload
   ```
2. Iniciar a aplicação frontend:
   ```powershell
   cd frontend
   npm run dev
   ```
3. Acessar `http://localhost:5173` no navegador:
   - Navegar até a aba de **Perfil**.
   - Preencher nome, headline, contatos e cargos-alvo.
   - Adicionar uma experiência profissional e uma competência técnica.
   - Colar texto de currículo na seção "Currículo-Base Bruto".
   - Clicar em "Salvar Alterações" e verificar a mensagem de sucesso.
   - Recarregar a página (F5) e atestar a persistência de 100% dos dados.
