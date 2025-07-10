from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_create_bearer_tokens_request import AuthCreateBearerTokensRequest
from ...models.auth_create_bearer_tokens_response import AuthCreateBearerTokensResponse
from ...models.common_rest_error import CommonRestError
from ...types import Response


def _get_kwargs(
    *,
    body: AuthCreateBearerTokensRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/bearerTokens",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AuthCreateBearerTokensResponse, CommonRestError]]:
    if response.status_code == 200:
        response_200 = AuthCreateBearerTokensResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CommonRestError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = CommonRestError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = CommonRestError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AuthCreateBearerTokensResponse, CommonRestError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AuthCreateBearerTokensRequest,
) -> Response[Union[AuthCreateBearerTokensResponse, CommonRestError]]:
    """Add one or more bearer tokens.

     Add one or more bearer tokens for the user.

    Args:
        body (AuthCreateBearerTokensRequest): Create one or more new bearer tokens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthCreateBearerTokensResponse, CommonRestError]]
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
    client: AuthenticatedClient,
    body: AuthCreateBearerTokensRequest,
) -> Optional[Union[AuthCreateBearerTokensResponse, CommonRestError]]:
    """Add one or more bearer tokens.

     Add one or more bearer tokens for the user.

    Args:
        body (AuthCreateBearerTokensRequest): Create one or more new bearer tokens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthCreateBearerTokensResponse, CommonRestError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AuthCreateBearerTokensRequest,
) -> Response[Union[AuthCreateBearerTokensResponse, CommonRestError]]:
    """Add one or more bearer tokens.

     Add one or more bearer tokens for the user.

    Args:
        body (AuthCreateBearerTokensRequest): Create one or more new bearer tokens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthCreateBearerTokensResponse, CommonRestError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AuthCreateBearerTokensRequest,
) -> Optional[Union[AuthCreateBearerTokensResponse, CommonRestError]]:
    """Add one or more bearer tokens.

     Add one or more bearer tokens for the user.

    Args:
        body (AuthCreateBearerTokensRequest): Create one or more new bearer tokens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthCreateBearerTokensResponse, CommonRestError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
