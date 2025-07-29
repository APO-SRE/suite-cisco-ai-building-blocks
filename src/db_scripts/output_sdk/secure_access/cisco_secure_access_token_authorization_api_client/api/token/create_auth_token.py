from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_auth_token_body import CreateAuthTokenBody
from ...models.create_auth_token_response_400 import CreateAuthTokenResponse400
from ...models.create_auth_token_response_401 import CreateAuthTokenResponse401
from ...models.create_auth_token_response_403 import CreateAuthTokenResponse403
from ...models.create_auth_token_response_404 import CreateAuthTokenResponse404
from ...models.create_auth_token_response_500 import CreateAuthTokenResponse500
from ...models.token import Token
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAuthTokenBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/token",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        CreateAuthTokenResponse400,
        CreateAuthTokenResponse401,
        CreateAuthTokenResponse403,
        CreateAuthTokenResponse404,
        CreateAuthTokenResponse500,
        Token,
    ]
]:
    if response.status_code == 200:
        response_200 = Token.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CreateAuthTokenResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CreateAuthTokenResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CreateAuthTokenResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = CreateAuthTokenResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = CreateAuthTokenResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        CreateAuthTokenResponse400,
        CreateAuthTokenResponse401,
        CreateAuthTokenResponse403,
        CreateAuthTokenResponse404,
        CreateAuthTokenResponse500,
        Token,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAuthTokenBody,
) -> Response[
    Union[
        CreateAuthTokenResponse400,
        CreateAuthTokenResponse401,
        CreateAuthTokenResponse403,
        CreateAuthTokenResponse404,
        CreateAuthTokenResponse500,
        Token,
    ]
]:
    """Create Authorization Token

     Create an authorization token.

    Args:
        body (CreateAuthTokenBody): The authentication information that is required to create an
            access token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateAuthTokenResponse400, CreateAuthTokenResponse401, CreateAuthTokenResponse403, CreateAuthTokenResponse404, CreateAuthTokenResponse500, Token]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAuthTokenBody,
) -> Optional[
    Union[
        CreateAuthTokenResponse400,
        CreateAuthTokenResponse401,
        CreateAuthTokenResponse403,
        CreateAuthTokenResponse404,
        CreateAuthTokenResponse500,
        Token,
    ]
]:
    """Create Authorization Token

     Create an authorization token.

    Args:
        body (CreateAuthTokenBody): The authentication information that is required to create an
            access token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateAuthTokenResponse400, CreateAuthTokenResponse401, CreateAuthTokenResponse403, CreateAuthTokenResponse404, CreateAuthTokenResponse500, Token]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAuthTokenBody,
) -> Response[
    Union[
        CreateAuthTokenResponse400,
        CreateAuthTokenResponse401,
        CreateAuthTokenResponse403,
        CreateAuthTokenResponse404,
        CreateAuthTokenResponse500,
        Token,
    ]
]:
    """Create Authorization Token

     Create an authorization token.

    Args:
        body (CreateAuthTokenBody): The authentication information that is required to create an
            access token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateAuthTokenResponse400, CreateAuthTokenResponse401, CreateAuthTokenResponse403, CreateAuthTokenResponse404, CreateAuthTokenResponse500, Token]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAuthTokenBody,
) -> Optional[
    Union[
        CreateAuthTokenResponse400,
        CreateAuthTokenResponse401,
        CreateAuthTokenResponse403,
        CreateAuthTokenResponse404,
        CreateAuthTokenResponse500,
        Token,
    ]
]:
    """Create Authorization Token

     Create an authorization token.

    Args:
        body (CreateAuthTokenBody): The authentication information that is required to create an
            access token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateAuthTokenResponse400, CreateAuthTokenResponse401, CreateAuthTokenResponse403, CreateAuthTokenResponse404, CreateAuthTokenResponse500, Token]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
