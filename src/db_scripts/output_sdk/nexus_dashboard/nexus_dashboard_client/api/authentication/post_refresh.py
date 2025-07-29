from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_refresh_response_200 import PostRefreshResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    auth_cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    cookies = {}
    if auth_cookie is not UNSET:
        cookies["AuthCookie"] = auth_cookie

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/refresh",
        "cookies": cookies,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostRefreshResponse200]:
    if response.status_code == 200:
        response_200 = PostRefreshResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostRefreshResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    auth_cookie: Union[Unset, str] = UNSET,
) -> Response[PostRefreshResponse200]:
    """Refresh Authentication Token

     Refreshes an existing authentication token.
    Authentication tokens are valid for a specific period of time and you must refresh it if you want to
    continue using the token beyond the configured duration. You can change the default token duration
    in the Nexus Dashboard UI.

    Args:
        auth_cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRefreshResponse200]
    """

    kwargs = _get_kwargs(
        auth_cookie=auth_cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    auth_cookie: Union[Unset, str] = UNSET,
) -> Optional[PostRefreshResponse200]:
    """Refresh Authentication Token

     Refreshes an existing authentication token.
    Authentication tokens are valid for a specific period of time and you must refresh it if you want to
    continue using the token beyond the configured duration. You can change the default token duration
    in the Nexus Dashboard UI.

    Args:
        auth_cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRefreshResponse200
    """

    return sync_detailed(
        client=client,
        auth_cookie=auth_cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    auth_cookie: Union[Unset, str] = UNSET,
) -> Response[PostRefreshResponse200]:
    """Refresh Authentication Token

     Refreshes an existing authentication token.
    Authentication tokens are valid for a specific period of time and you must refresh it if you want to
    continue using the token beyond the configured duration. You can change the default token duration
    in the Nexus Dashboard UI.

    Args:
        auth_cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRefreshResponse200]
    """

    kwargs = _get_kwargs(
        auth_cookie=auth_cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    auth_cookie: Union[Unset, str] = UNSET,
) -> Optional[PostRefreshResponse200]:
    """Refresh Authentication Token

     Refreshes an existing authentication token.
    Authentication tokens are valid for a specific period of time and you must refresh it if you want to
    continue using the token beyond the configured duration. You can change the default token duration
    in the Nexus Dashboard UI.

    Args:
        auth_cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRefreshResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            auth_cookie=auth_cookie,
        )
    ).parsed
