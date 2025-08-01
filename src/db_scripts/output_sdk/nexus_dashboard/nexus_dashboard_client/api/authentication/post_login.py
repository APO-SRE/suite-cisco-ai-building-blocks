from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_login_body import PostLoginBody
from ...models.post_login_response_200 import PostLoginResponse200
from ...models.post_login_response_401 import PostLoginResponse401
from ...types import Response


def _get_kwargs(
    *,
    body: PostLoginBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/login",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json; charset=utf-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostLoginResponse200, PostLoginResponse401]]:
    if response.status_code == 200:
        response_200 = PostLoginResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = PostLoginResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostLoginResponse200, PostLoginResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostLoginBody,
) -> Response[Union[PostLoginResponse200, PostLoginResponse401]]:
    """Login

     Returns an authentication token, which can be used for subsequent API calls.
    You can provide a username, password, and login domain to authenticate an existing Nexus Dashboard
    user.

    Args:
        body (PostLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostLoginResponse200, PostLoginResponse401]]
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
    body: PostLoginBody,
) -> Optional[Union[PostLoginResponse200, PostLoginResponse401]]:
    """Login

     Returns an authentication token, which can be used for subsequent API calls.
    You can provide a username, password, and login domain to authenticate an existing Nexus Dashboard
    user.

    Args:
        body (PostLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostLoginResponse200, PostLoginResponse401]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostLoginBody,
) -> Response[Union[PostLoginResponse200, PostLoginResponse401]]:
    """Login

     Returns an authentication token, which can be used for subsequent API calls.
    You can provide a username, password, and login domain to authenticate an existing Nexus Dashboard
    user.

    Args:
        body (PostLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostLoginResponse200, PostLoginResponse401]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostLoginBody,
) -> Optional[Union[PostLoginResponse200, PostLoginResponse401]]:
    """Login

     Returns an authentication token, which can be used for subsequent API calls.
    You can provide a username, password, and login domain to authenticate an existing Nexus Dashboard
    user.

    Args:
        body (PostLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostLoginResponse200, PostLoginResponse401]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
